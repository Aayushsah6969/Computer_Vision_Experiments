import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Define ROI (right half of the frame)
    x_start = w // 2
    y_start = 0
    x_end = w
    y_end = h

    roi = frame[y_start:y_end, x_start:x_end]

    # Draw ROI rectangle for user guidance
    cv2.rectangle(frame, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
    cv2.putText(frame, "Put hand here", (x_start + 10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # Convert ROI to HSV for skin detection
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Skin color range (tune if needed)
    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([20, 255, 255], dtype=np.uint8)
    mask = cv2.inRange(hsv, lower, upper)

    # Clean mask
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    finger_count = 0

    if contours:
        # Take largest contour in ROI
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)

        # Area filter: avoid tiny noise or huge blobs
        if 5000 < area < 80000:
            # Draw contour on original frame (shift by x_start, y_start)
            cnt_shifted = cnt + np.array([[[x_start, y_start]]])
            cv2.drawContours(frame, [cnt_shifted], -1, (0, 255, 0), 2)

            # Convex hull and defects
            hull = cv2.convexHull(cnt, returnPoints=False)
            if hull is not None and len(hull) > 3:
                defects = cv2.convexityDefects(cnt, hull)

                if defects is not None:
                    valid_gaps = 0
                    for i in range(defects.shape[0]):
                        s, e, f, d = defects[i, 0]
                        start = tuple(cnt[s][0])
                        end = tuple(cnt[e][0])
                        far = tuple(cnt[f][0])

                        # Compute triangle sides
                        a = np.linalg.norm(np.array(end) - np.array(start))
                        b = np.linalg.norm(np.array(far) - np.array(start))
                        c = np.linalg.norm(np.array(end) - np.array(far))

                        # Avoid division error
                        if b * c == 0:
                            continue

                        # Cosine rule for angle at far point
                        angle = np.degrees(np.arccos((b**2 + c**2 - a**2) / (2 * b * c)))

                        # Use depth and angle to filter real finger gaps
                        if d > 10000 and angle < 90:
                            valid_gaps += 1
                            # Draw defect point (shifted)
                            far_shifted = (far[0] + x_start, far[1] + y_start)
                            cv2.circle(frame, far_shifted, 5, (255, 0, 0), -1)

                    finger_count = valid_gaps + 1  # gaps + 1 ≈ fingers

    # Show finger count
    cv2.putText(frame, f"Fingers: {finger_count}", (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Finger Counter (ROI + Improved)", frame)
    cv2.imshow("Mask (ROI)", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

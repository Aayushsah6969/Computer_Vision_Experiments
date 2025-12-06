import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert to HSV for skin detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range (approx.)
    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower, upper)

    # Blur to remove noise
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Largest contour = hand
        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        # Draw contour
        cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 2)

        # Convex hull
        hull = cv2.convexHull(cnt)

        cv2.drawContours(frame, [hull], -1, (0, 0, 255), 2)

        # Convexity defects
        hull_indices = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt, hull_indices)

        finger_count = 0

        if defects is not None:
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])

                # If defect is deep → finger gap
                if d > 10000:
                    finger_count += 1
                    cv2.circle(frame, far, 5, (255, 0, 0), -1)

            finger_count += 1  # one more finger than gaps

        cv2.putText(frame, f"Fingers: {finger_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Finger Counter (OpenCV Only)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

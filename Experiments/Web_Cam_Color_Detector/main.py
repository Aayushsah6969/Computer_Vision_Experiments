import cv2
import numpy as np

# Predefined basic colors dictionary
colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
    "Gray": (128, 128, 128)
}

def get_color_name(rgb):
    min_dist = float("inf")
    color_name = "Unknown"
    for name, value in colors.items():
        dist = np.linalg.norm(np.array(rgb) - np.array(value))
        if dist < min_dist:
            min_dist = dist
            color_name = name
    return color_name

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    h, w, _ = frame.shape
    cx, cy = w // 2, h // 2  # center pixel

    # Get color of center pixel
    b, g, r = frame[cy, cx]
    rgb = (r, g, b)

    # Get nearest color name
    cname = get_color_name(rgb)

    # Draw a circle at the center
    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

    # Display color info on screen
    text = f"{cname}  RGB({r}, {g}, {b})"
    cv2.putText(frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Show real-time frame
    cv2.imshow("Color Detector", frame)

    # Exit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

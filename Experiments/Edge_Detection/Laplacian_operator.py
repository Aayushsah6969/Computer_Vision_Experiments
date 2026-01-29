import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

# optional smoothing (recommended)
blur = cv2.GaussianBlur(img, (3,3), 0)

# Laplacian
laplacian = cv2.Laplacian(blur, cv2.CV_64F)

laplacian = cv2.convertScaleAbs(laplacian)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1); plt.title("Original"); plt.imshow(img, cmap='gray')
plt.subplot(1,2,2); plt.title("Laplacian"); plt.imshow(laplacian, cmap='gray')
plt.show()

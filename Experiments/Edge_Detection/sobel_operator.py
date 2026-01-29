import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

# Sobel X and Y
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# gradient magnitude
sobel_mag = np.sqrt(sobel_x**2 + sobel_y**2)

# normalize for display
sobel_mag = cv2.normalize(sobel_mag, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(10,4))
plt.subplot(1,3,1); plt.title("Original"); plt.imshow(img, cmap='gray')
plt.subplot(1,3,2); plt.title("Sobel X"); plt.imshow(np.abs(sobel_x), cmap='gray')
plt.subplot(1,3,3); plt.title("Sobel Magnitude"); plt.imshow(sobel_mag, cmap='gray')
plt.show()

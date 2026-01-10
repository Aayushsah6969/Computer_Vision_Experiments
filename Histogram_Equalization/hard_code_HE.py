import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read grayscale image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError("Image not found")

# Step 1: Compute histogram manually
hist = [0] * 256
rows, cols = img.shape

for i in range(rows):
    for j in range(cols):
        intensity = img[i][j]
        hist[intensity] += 1

# Step 2: Compute CDF manually
cdf = [0] * 256
cdf[0] = hist[0]

for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]

# Step 3: Normalize CDF
cdf_min = next(value for value in cdf if value != 0)
total_pixels = rows * cols

cdf_normalized = [0] * 256
for i in range(256):
    cdf_normalized[i] = round(
        (cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255
    )

# Step 4: Map old pixel values to new values
equalized = np.zeros_like(img)

for i in range(rows):
    for j in range(cols):
        equalized[i][j] = cdf_normalized[img[i][j]]

# Display results
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Histogram Equalized Image")
plt.imshow(equalized, cmap='gray')
plt.axis('off')

plt.show()

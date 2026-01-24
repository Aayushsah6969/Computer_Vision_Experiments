import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Load image (grayscale)
# ----------------------------
image = cv2.imread("image.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found. Check file path.")

# ----------------------------
# 1. Min Filter (Erosion)
# ----------------------------
kernel = np.ones((3, 3), np.uint8)
min_filtered = cv2.erode(image, kernel)

# ----------------------------
# 2. Max Filter (Dilation)
# ----------------------------
max_filtered = cv2.dilate(image, kernel)

# ----------------------------
# 3. Median Filter
# ----------------------------
median_filtered = cv2.medianBlur(image, 3)

# ----------------------------
# 4. Average (Mean) Filter
# ----------------------------
average_filtered = cv2.blur(image, (3, 3))

# ----------------------------
# 5. Weighted Average Filter (Gaussian)
# ----------------------------
weighted_average_filtered = cv2.GaussianBlur(image, (3, 3), 0)

# ----------------------------
# Display results
# ----------------------------
titles = [
    "Original Image",
    "Min Filter",
    "Max Filter",
    "Median Filter",
    "Average Filter",
    "Weighted Average Filter"
]

images = [
    image,
    min_filtered,
    max_filtered,
    median_filtered,
    average_filtered,
    weighted_average_filtered
]

plt.figure(figsize=(12, 8))

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()

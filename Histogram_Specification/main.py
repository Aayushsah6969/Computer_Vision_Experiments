import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

source_path = os.path.join(BASE_DIR, "source.jpeg")
reference_path = os.path.join(BASE_DIR, "reference.jpeg")

source = cv2.imread(source_path, cv2.IMREAD_GRAYSCALE)
reference = cv2.imread(reference_path, cv2.IMREAD_GRAYSCALE)

if source is None:
    raise ValueError(f"Source image not found at: {source_path}")

if reference is None:
    raise ValueError(f"Reference image not found at: {reference_path}")


# ---------------------------
# Step 2: Compute histograms
# ---------------------------
def compute_histogram(image):
    hist = np.zeros(256)
    for pixel in image.flatten():
        hist[pixel] += 1
    return hist

source_hist = compute_histogram(source)
ref_hist = compute_histogram(reference)

# ---------------------------
# Step 3: Compute CDFs
# ---------------------------
def compute_cdf(hist):
    cdf = hist.cumsum()
    cdf = cdf / cdf[-1]   # normalize
    return cdf

source_cdf = compute_cdf(source_hist)
ref_cdf = compute_cdf(ref_hist)

# ---------------------------
# Step 4: Create mapping
# ---------------------------
mapping = np.zeros(256, dtype=np.uint8)

for i in range(256):
    diff = np.abs(source_cdf[i] - ref_cdf)
    mapping[i] = np.argmin(diff)

# ---------------------------
# Step 5: Apply mapping
# ---------------------------
matched = mapping[source]

# ---------------------------
# Step 6: Display results
# ---------------------------
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.title("Source Image")
plt.imshow(source, cmap='gray')
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Reference Image")
plt.imshow(reference, cmap='gray')
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Histogram Specified Image")
plt.imshow(matched, cmap='gray')
plt.axis("off")

plt.show()

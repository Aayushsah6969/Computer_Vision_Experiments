import cv2
import matplotlib.pyplot as plt

img = cv2.imread(
    r"C:\Users\aayus\Desktop\Study Materials\CV\Experiments\Histogram_Equalization\image.jpg",
    cv2.IMREAD_GRAYSCALE
)


if img is None:
    raise FileNotFoundError("Image not found. Check the file path.")

equalized = cv2.equalizeHist(img)

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

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title("Original Histogram")
plt.hist(img.flatten(), bins=256)

plt.subplot(1,2,2)
plt.title("Equalized Histogram")
plt.hist(equalized.flatten(), bins=256)

plt.show()

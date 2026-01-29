from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# 1. Load your local image
# Replace the path with the location of your photo
img = Image.open("photo.jpeg")

# 2. Convert to grayscale
gray_img = img.convert("L")   # "L" means grayscale (8-bit pixels)

# 3. Show the grayscale image
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# Convert grayscale image to a numpy array (2D matrix)
gray_matrix = np.array(gray_img)

# Print the matrix
print(gray_matrix)
gray_img.save("gray_photo.jpg")

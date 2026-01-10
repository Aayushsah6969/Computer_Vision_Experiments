# Histogram Equalization

## What is Histogram Equalization?

Histogram Equalization is an image processing technique used to improve the contrast of an image by redistributing the intensity values. It works by spreading out the most frequent intensity values across the entire range of pixel intensities (0-255 for 8-bit images), effectively transforming the histogram to be more uniform.

The technique uses a cumulative distribution function (CDF) to map the original intensity values to new values that are more evenly distributed across the available range.

## Why is it Used?

Histogram equalization is used to enhance images that have poor contrast due to:
- **Under-exposure or over-exposure** during image capture
- **Poor lighting conditions** where the image appears too dark or too bright
- **Limited dynamic range** where pixel intensities are concentrated in a narrow range
- **Washed out images** where details are not clearly visible

By redistributing pixel intensities, histogram equalization makes hidden features and details more visible, improving the overall visual quality of the image.

## Advantages

1. **Automatic Enhancement**: No manual tuning of parameters required - it's a fully automatic process
2. **Improved Contrast**: Significantly enhances contrast in low-contrast images
3. **Better Feature Visibility**: Makes subtle details and features more visible
4. **Simple Implementation**: Easy to implement and computationally efficient
5. **Universal Application**: Works well on various types of images including medical, satellite, and natural images
6. **Preprocessing Benefits**: Improves performance of other image processing algorithms like edge detection and segmentation

## Uses and Applications

- **Medical Imaging**: Enhancing X-rays, CT scans, and MRI images to reveal subtle abnormalities
- **Satellite and Aerial Imaging**: Improving visibility of terrain features and land patterns
- **Photography**: Correcting under-exposed or over-exposed photographs
- **Computer Vision**: Preprocessing step for object detection, facial recognition, and pattern recognition
- **Surveillance**: Enhancing low-light security camera footage
- **Document Processing**: Improving readability of scanned documents
- **Scientific Research**: Analyzing microscopy images and astronomical photographs

## What We Have Done in This Project

This project demonstrates histogram equalization on grayscale images using OpenCV and Python. The implementation includes:

### Features:
1. **Image Loading**: Reads a grayscale image from the file system
2. **Histogram Equalization**: Applies `cv2.equalizeHist()` function to enhance image contrast
3. **Visual Comparison**: Displays both original and equalized images side-by-side
4. **Histogram Analysis**: Plots histograms of both images to visualize the intensity distribution changes

### Implementation Details:
- Uses OpenCV's built-in `equalizeHist()` function for efficient histogram equalization
- Employs Matplotlib for visualization of images and histograms
- Compares original vs. equalized images to demonstrate the enhancement effect
- Shows how pixel intensity distribution changes after equalization

### How It Works:
1. Load a grayscale image using `cv2.imread()` with `cv2.IMREAD_GRAYSCALE` flag
2. Apply histogram equalization using `cv2.equalizeHist()`
3. Display original and equalized images side-by-side
4. Plot histograms showing the intensity distribution before and after equalization

### Results:
The output clearly demonstrates how histogram equalization redistributes pixel intensities to improve contrast, making the image details more visible and the histogram more uniformly distributed.

## Requirements

- OpenCV (`cv2`)
- Matplotlib
- NumPy (implicitly required by OpenCV)

## Usage

```python
python main.py
```

Make sure to update the image path in the code to point to your desired input image.

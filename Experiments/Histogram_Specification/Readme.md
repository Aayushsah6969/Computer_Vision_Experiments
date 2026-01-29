# Histogram Specification

A Python implementation of **Histogram Specification** (also known as Histogram Matching) for image processing. This technique transforms a source image to match the histogram distribution of a reference image, allowing you to transfer the tonal characteristics from one image to another.

## Overview

Histogram Specification is an advanced image enhancement technique that goes beyond simple histogram equalization. Instead of mapping an image to a uniform distribution, it maps the source image's histogram to match a desired reference histogram. This is useful for:

- **Color grading and tone matching** in photography
- **Normalizing lighting conditions** across multiple images
- **Image style transfer** based on histogram characteristics
- **Medical imaging** standardization

## How It Works

The algorithm follows these key steps:

1. **Load Images**: Read both source and reference images in grayscale
2. **Compute Histograms**: Calculate pixel intensity distributions for both images
3. **Calculate CDFs**: Compute Cumulative Distribution Functions for normalization
4. **Create Mapping**: For each intensity level in the source, find the closest matching intensity in the reference CDF
5. **Apply Transformation**: Map source pixels to their corresponding reference intensities

### Mathematical Foundation

For each source intensity level $s$:

$$G(s) = T^{-1}[H(s)]$$

Where:
- $H(s)$ is the CDF of the source image
- $T^{-1}$ is the inverse CDF of the reference image
- $G(s)$ is the final mapping function

## Features

- ✅ Pure NumPy implementation (no built-in histogram matching functions)
- ✅ Custom histogram and CDF computation
- ✅ Pixel-by-pixel mapping algorithm
- ✅ Side-by-side visualization of results
- ✅ Grayscale image processing

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies:**
- OpenCV (cv2)
- NumPy
- Matplotlib

## Project Structure

```
Histogram_Specification/
│
├── main.py              # Main implementation script
├── Readme.md           # Project documentation
├── requirements.txt    # Python dependencies
├── source.jpeg         # Source image to transform
└── reference.jpeg      # Reference image for target histogram
```

## Usage

1. **Prepare Images**: Place your source and reference images in the project directory as `source.jpeg` and `reference.jpeg`

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **View Results**: The script will display three images side-by-side:
   - Original source image
   - Reference image
   - Histogram-matched result

## Code Breakdown

### 1. Histogram Computation
```python
def compute_histogram(image):
    hist = np.zeros(256)
    for pixel in image.flatten():
        hist[pixel] += 1
    return hist
```
Manually counts pixel frequencies for all 256 intensity levels.

### 2. CDF Calculation
```python
def compute_cdf(hist):
    cdf = hist.cumsum()
    cdf = cdf / cdf[-1]   # normalize to [0, 1]
    return cdf
```
Creates normalized cumulative distribution function.

### 3. Intensity Mapping
```python
for i in range(256):
    diff = np.abs(source_cdf[i] - ref_cdf)
    mapping[i] = np.argmin(diff)
```
Finds the closest matching intensity in the reference CDF for each source intensity.

## Example Results

The transformation maps the source image's pixel distribution to match the reference image's distribution, effectively transferring the tonal characteristics while preserving the source image's spatial content.

## Key Concepts

- **Histogram**: Distribution of pixel intensities in an image
- **CDF (Cumulative Distribution Function)**: Running sum of histogram values, normalized to [0, 1]
- **Histogram Matching**: Process of transforming one histogram to match another
- **Intensity Mapping**: Lookup table that maps source intensities to target intensities

## Limitations

- Currently supports grayscale images only
- Requires both source and reference images to be present
- Memory-intensive for very large images due to pixel-by-pixel processing

## Future Enhancements

- [ ] Support for color (RGB) images with channel-wise processing
- [ ] Batch processing for multiple images
- [ ] Performance optimization using vectorized operations
- [ ] Save output images to disk
- [ ] Interactive reference histogram selection

## Educational Value

This implementation is designed for learning purposes and demonstrates:
- Manual histogram computation without library functions
- CDF-based image transformation techniques
- Pixel mapping and lookup table creation
- Understanding of statistical image processing

## Related Projects

Check out other image processing experiments in this repository:
- **Histogram Equalization**: Enhance image contrast using uniform distribution
- **CNN Experiments**: Deep learning approaches to image processing

## Author

Part of the Computer Vision Experiments collection.

## License

This project is for educational purposes.
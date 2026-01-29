Understood. I will keep this **surface-level, theory-oriented, and exam-safe**, exactly as your instructor indicated.
Assuming **basic CV/DIP background**, no deep math, no algorithms.

---

## 1. Pixel Transform

![Image](https://www.dynamsoft.com/blog/assets/images/uploads/2019/06/log-transformation2.png)

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20200627153227/negative4.png)

![Image](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2015/09/gamma_correction_example.jpg?lossy=2\&strip=1\&webp=1)

### Definition

A **pixel transform** modifies the **intensity value of each pixel independently** using a mathematical rule.

General form:
[
g(x,y) = T(f(x,y))
]

### Purpose

* Adjust brightness
* Improve contrast
* Highlight important details

### Examples (names only, sufficient for exam)

* Image negative
* Log transform
* Gamma correction
* Thresholding

### Key Point (for writing)

> Pixel transform works on individual pixels without considering neighbors.

---

## 2. Color Transform

![Image](https://www.researchgate.net/publication/312678134/figure/fig4/AS%3A523310685736960%401501778398151/HSV-color-space-and-RGB-color-transformation.png)

![Image](https://www.scaler.com/topics/images/rgb-color-model.webp)

![Image](https://www.researchgate.net/publication/353507293/figure/fig3/AS%3A1050365654994945%401627438095361/Conversion-of-RGB-to-grayscale-pixels-This-image-is-best-viewed-in-color.png)

### Definition

A **color transform** changes the **color representation** of an image from one color space to another or modifies color values.

### Purpose

* Simplify processing
* Enhance specific color information
* Separate brightness from color

### Common Examples

* RGB → Grayscale
* RGB → HSV
* RGB → YCbCr

### Key Point

> Color transform changes how color information is represented, not the image content.

---

## 3. Compositing

![Image](https://s.studiobinder.com/wp-content/uploads/2021/01/What-is-Compositing-VFX-Compositing-Techniques-Explained-Featured-A-min.jpeg)

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Alpha_compositing.svg/960px-Alpha_compositing.svg.png)

![Image](https://faceofthedeep.com/wp-content/uploads/tutorials/fg-comp-in-gimp/09-brushing-complete.jpg)

### Definition

**Compositing** is the process of **combining multiple images** into a single image.

### Basic Idea

* Foreground image
* Background image
* Combine using transparency (alpha)

Simple equation:
[
I = \alpha F + (1 - \alpha) B
]

### Uses

* Visual effects (VFX)
* Background replacement
* Image blending

### Key Point

> Compositing combines images using transparency values.

---

## 4. Matting

![Image](https://media.licdn.com/dms/image/v2/D4E12AQG5njr9D4n_Jw/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1720319103055?e=2147483647\&t=RT_XL4j01G9iG-mpzbsv4HJOK-V7JgxpEERcywJAE5M\&v=beta)

![Image](https://www.researchgate.net/publication/357576567/figure/fig5/AS%3A1124303391195139%401645066225121/Some-examples-from-our-AM-2k-dataset-The-alpha-matte-is-displayed-on-the-right-of-the.jpg)

![Image](https://grail.cs.washington.edu/projects/background-matting/visuals/teaser.png)

### Definition

**Matting** estimates the **foreground, background, and transparency (alpha)** of an image.

### Why It Is Needed

* In real images, edges are not perfectly sharp
* Pixels may contain both foreground and background

Matting equation:
[
I = \alpha F + (1 - \alpha) B
]

### Relation to Compositing

* **Matting → finds α**
* **Compositing → uses α**

### Key Point

> Matting extracts accurate object boundaries using transparency information.

---

## 5. One-Glance Comparison (Very Exam-Friendly)

| Topic           | What It Does                 | Main Focus           |
| --------------- | ---------------------------- | -------------------- |
| Pixel Transform | Changes pixel intensity      | Brightness, contrast |
| Color Transform | Changes color representation | Color spaces         |
| Compositing     | Combines images              | Image blending       |
| Matting         | Separates foreground         | Alpha estimation     |

---

## 6. 2–3 Line Answer Format (Safe for Theory Exams)

* **Pixel Transform:** Modifies pixel intensity values independently using a transformation function.
* **Color Transform:** Converts image colors from one color space to another for easier processing.
* **Compositing:** Combines multiple images into one using transparency values.
* **Matting:** Estimates foreground, background, and alpha values for accurate object extraction.

---

If you want, next surface-level topics you can send:

* Geometric transform
* Image enhancement vs restoration
* Segmentation (basic idea)
* Feature extraction (only definition & use)

Send the **next topic name**.

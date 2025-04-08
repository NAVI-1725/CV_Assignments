# Assignment 1: Image Processing Report
**Name:** Penumarthi Navya Sree Ram Kumar Chowdary  
**Roll Number:** CS22B1039  
**Course:** Computer Vision  
**Institute:** IIIT Raichur

---

## Task 2: Image Processing

### 1. Objective
To apply classic image processing techniques to enhance and analyze an image using OpenCV.

---

### 2. Steps Performed

#### a. Grayscale Conversion
Converted the original color image to grayscale to reduce complexity.

#### b. Histogram Equalization
Enhanced contrast of the grayscale image using `cv2.equalizeHist()`.

#### c. Gaussian Blur
Reduced noise and smoothed the image using a 5x5 Gaussian kernel.

#### d. Canny Edge Detection
Detected strong edges using the Canny method with thresholds of 50 and 150.

#### e. Morphological Dilation
Emphasized detected edges by dilating them using a 3x3 rectangular kernel.

#### f. Watermarking
Overlayed my full name on the final image as a watermark.

---

### 3. Output Samples

| Step               | Image              |
|--------------------|--------------------|
| Grayscale          | `gray.jpg`         |
| Histogram Equalized| `hist_eq.jpg`      |
| Edges              | `edges.jpg`        |
| Final Dilated Edge | `dilated_with_name.jpg` |
| Demo Video         | `demo_video.mp4`   |

---

### 4. Code Link
Refer to `task2_image_processing.py` and `generate_demo_video.py` in the `code/` directory.

---

### 5. Observations
- Histogram Equalization improves detail in dark/light areas.
- Canny edge detection is sensitive to noise — hence Gaussian Blur is important.
- Morphological operations help refine the detected features.

---

### 6. Learnings
- Practical usage of OpenCV’s core functionalities.
- Structured approach to image preprocessing.
- Importance of step-wise debugging and visual verification.

---

## End of Report ✅

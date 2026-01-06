## Color Object Detection and Tracking using OpenCV

A real-time color-based object detection and tracking system using OpenCV and HSV color space through a webcam.

---

### About the Project

This project demonstrates real-time color object detection and tracking using computer vision techniques.  
It captures live video from a webcam, converts frames into HSV color space, applies color masking, detects contours, and tracks the object’s position and movement direction.

The system can also determine basic movement commands such as **Left, Right, Front, and Stop** based on the detected object’s position and size.

---

### Features

- Real-time color object detection using webcam  
- HSV-based color masking  
- Object tracking with contour detection  
- Center and radius calculation of detected object  
- Direction detection (Left / Right / Front / Stop)  
- Interactive HSV value tuning using trackbars  

---

### Technologies Used

- Python  
- OpenCV  
- NumPy  
- Imutils  

---

### How to Run

1. Run HSV mask calibration to find color values:
   ```bash
   python mask_hsv.py
   
2. Update HSV values in the main script if needed.

3. Run the color detection and tracking program:
   ```bash
   python main.py
   
4. Press ESC to exit the application.
  
---

### Project Folder Structure

color-object-detection-tracking-opencv/
│
├── main.py                 # Color detection and tracking script
├── mask_hsv.py             # HSV value calibration using trackbars
├── README.md               # Project documentation
├── requirements.txt        # Required libraries
└── assets/                 # Sample outputs (optional)

---

## Working Principle

- Capture live video frames using a webcam  
- Resize and blur frames to reduce noise  
- Convert frames from BGR to HSV color space  
- Apply HSV color thresholding to create a mask  
- Perform erosion and dilation to remove noise  
- Detect contours from the masked image  
- Track the largest detected object  
- Calculate object center and radius  
- Determine movement direction based on position and size  

---

## Applications

- Color-based object tracking systems  
- Robotics navigation (basic direction control)  
- Surveillance and monitoring  
- Human–computer interaction  
- Learning computer vision fundamentals  

---

## Output

- Real-time webcam feed with detected color object  
- Bounding circle and center point visualization  
- Console output indicating movement direction  
- Masked view showing detected color region  

---

### License

This project is intended for educational purposes.

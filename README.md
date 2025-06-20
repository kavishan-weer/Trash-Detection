# Trash Detection System

A real-time trash detection system using YOLOv5 and OpenCV, optimized for Raspberry Pi and other edge devices.

## Features

- Real-time object detection using YOLOv5
- Optimized for CPU inference
- Live webcam feed with bounding box visualization
- FPS monitoring
- Configurable confidence threshold

## Requirements

### Hardware
- Computer with webcam or Raspberry Pi with camera module
- Minimum 4GB RAM recommended
- USB camera (if not using built-in camera)

### Software
- Python 3.7+
- PyTorch
- OpenCV
- YOLOv5 dependencies

## Installation

### 1. Clone the Repository
git clone https://github.com/kavishan-weer/trash-detection.git
cd trash-detection

### 2. Clone the Repository
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..

### 3. Run the Detection Script
python detect.py
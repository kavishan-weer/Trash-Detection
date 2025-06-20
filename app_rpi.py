import torch
import cv2
import time
from ultralytics import YOLO

@torch.no_grad()
def run_detection():
    # Load model using ultralytics YOLO
    model = YOLO('best.pt')  # Much simpler!
    
    # Set confidence threshold
    model.conf = 0.5
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Calculate FPS
    prev_time = time.time()
    fps_counter = 0
    fps = 0
    
    print("Starting detection - press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Update FPS calculation
        fps_counter += 1
        if time.time() - prev_time >= 1.0:
            fps = fps_counter
            fps_counter = 0
            prev_time = time.time()
            print(f"FPS: {fps}")
        
        # Run inference
        results = model(frame, imgsz=640, verbose=False)
        
        # Print debug info
        if fps_counter % 10 == 0:
            print(f'Detections: {len(results[0].boxes) if results[0].boxes is not None else 0}')
        
        # Draw results on frame
        annotated_frame = results[0].plot()
        
        # Add FPS counter
        cv2.putText(annotated_frame, f"FPS: {fps}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Trash Detection Webcam', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_detection()
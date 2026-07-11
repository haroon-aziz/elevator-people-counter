import os
import cv2
from ultralytics import solutions

VIDEO_SOURCE = "elevator_feed.mp4"
OUTPUT_PATH = "elevator_monitoring.mp4"  

cap = cv2.VideoCapture(VIDEO_SOURCE)
assert cap.isOpened(), "Error reading video file"

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fps = fps if fps > 0 else 25 

video_writer = cv2.VideoWriter(OUTPUT_PATH, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

line_points = [(int(0.08 * w), int(0.6 * h)), (int(0.92 * w), int(0.6 * h))]

show_live = bool(os.environ.get("DISPLAY")) or os.name == "nt"

counter = solutions.ObjectCounter(
    show=show_live,
    region=line_points,
    model="yolo26n.pt",
    classes=[0], 
)

try:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = counter(frame)
        video_writer.write(results.plot_im)

        
finally:
    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

print(f"Final counts -> In: {counter.in_count}, Out: {counter.out_count}")
print(f"Per-class breakdown: {dict(counter.classwise_count)}")

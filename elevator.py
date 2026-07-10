import cv2
from ultralytics import solutions

# Path to the input video (update this to your own elevator camera feed)
VIDEO_SOURCE = "elevator_feed.mp4"
OUTPUT_PATH = "elevator_monitoring.avi"

# Initialize video capture
cap = cv2.VideoCapture(VIDEO_SOURCE)
assert cap.isOpened(), "Error reading video file"

# Get video properties for output saving
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter(OUTPUT_PATH, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Define counting line (adjust coordinates to fit your elevator door)
line_points = [(100, 400), (1180, 400)]

# Initialize ObjectCounter with YOLO26
counter = solutions.ObjectCounter(
    show=True,
    region=line_points,
    model="yolo26n.pt",
    classes=[0]  # Class 0 is 'person' in COCO
)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Process frame and update counts
    processed_frame = counter(frame)
    video_writer.write(processed_frame.plot_im)

    # Access real-time analytics
    # print(f"Total In: {counter.in_counts} | Total Out: {counter.out_counts}")

cap.release()
video_writer.release()
cv2.destroyAllWindows()

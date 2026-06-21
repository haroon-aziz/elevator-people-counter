# Elevator People Counter

Real-time people counting and monitoring system for elevators, built using YOLO26 object detection and the Ultralytics `solutions` module. The script tracks people crossing a defined virtual line at the elevator door, counting entries (in) and exits (out) to help monitor occupancy and traffic patterns.

## Features

- Real-time person detection using YOLO26
- Line-crossing based in/out counting
- Works on pre-recorded video feeds (easily adaptable to live RTSP/webcam streams)
- Saves annotated output video with bounding boxes and live counts
- Lightweight — uses the `yolo26n.pt` (nano) model for fast inference

## How It Works

1. Captures video frames from the elevator camera feed (`elevator_feed.mp4`)
2. Runs YOLO26 detection restricted to the `person` class (COCO class 0)
3. Tracks each detected person and checks if they cross a defined line (`line_points`)
4. Increments in/out counters based on direction of crossing
5. Writes the annotated video to `elevator_monitoring.avi`

## Requirements

See `requirements.txt`. Main dependencies:

- Python 3.8+
- OpenCV
- Ultralytics (YOLO26 support)

## Installation

```bash
git clone https://github.com/haroon-aziz/elevator-people-counter.git
cd elevator-people-counter
pip install -r requirements.txt 
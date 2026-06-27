# Peace Sign Blur ✌️

A fun and interactive Python script that uses your webcam to detect a "peace" (✌️) hand sign. When you show a peace sign, the screen blurs automatically. Drop the sign, and the screen goes back to normal!

## Features
- **Real-time Hand Tracking**: Powered by [MediaPipe's](https://developers.google.com/mediapipe) Hand Landmarker task.
- **Dynamic Blur Effect**: Applies a Gaussian blur using [OpenCV](https://opencv.org/) whenever the peace sign is detected.

## Requirements
- Python 3.x
- `opencv-python`
- `mediapipe`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Adrobi251/kontent-peace.git
   cd kontent-peace
   ```
2. Install the required dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```
3. Make sure the MediaPipe hand landmarker model (`hand_landmarker.task`) is in the same directory as the script.

## Usage
Run the script using Python:
```bash
python blur.py
```
- Show a **peace sign (✌️)** to the camera to blur the screen.
- Press **`q`** to quit the application.

## How it Works
The script analyzes the hand landmarks detected by MediaPipe to determine if the peace sign is being made:
- Index and Middle fingers are UP (tip `y` < pip `y`).
- Ring and Pinky fingers are DOWN (tip `y` > pip `y`).

If this specific pose is detected, a `cv2.GaussianBlur` filter is applied to the frame.

## License
Feel free to use, modify, and share this code!

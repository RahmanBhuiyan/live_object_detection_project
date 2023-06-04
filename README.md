# Live Object Detection 

This repository provides an implementation of live object detection using the YOLOv4 algorithm. The aim is to detect and recognize objects in real-time using computer vision techniques and convert the detected objects into voice output.

## Features

- Real-time object detection: The system can detect objects in real-time, providing instant results.
- YOLOv4 algorithm: It utilizes the YOLOv4 algorithm, which is known for its high accuracy and efficiency.
- Webcam support: You can use the webcam to capture live video for object detection.
- Video stream support: The system can process video streams, allowing for object detection in pre-recorded videos or live streams.
- Multiple object detection: It can detect multiple objects simultaneously in a frame.
- High accuracy: The YOLOv4 model used achieves high accuracy in identifying and localizing objects.
- Voice output: The system can convert the detected objects into voice output, providing an audible description of the detected objects.

## Installation

To install and use the live object detection system with YOLOv4, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/RahmanBhuiyan/live_object_detection_project.git
   ```

2. Install the required dependencies. Make sure you have Python 3.6 or above installed. Run the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. Download the pre-trained YOLOv4 weights file. You can find the weights file from the official YOLOv4 repository or other reliable sources. Place the weights file in the repository's root directory.

4. Run the live object detection script:

   ```bash
   python main.py
   ```

   The script will start capturing the video stream from your webcam or any specified source, perform real-time object detection using YOLOv4, and provide voice output for the detected objects.

## Configuration

You can configure various parameters of the live object detection system by modifying the `config.py` file. Some of the available configurations include:

- Input source: Specify the video source (webcam, video file, or live stream URL).
- Model path: Set the path to the pre-trained YOLOv4 weights file.
- Confidence threshold: Adjust the minimum confidence score required for an object detection result to be considered valid.
- Output settings: Configure the visual output, such as bounding box colors and labels.

## Demo

To see the live object detection system in action with YOLOv4 and voice output, check out this [demo video](https://drive.google.com/file/d/10unDh5dgEp2L9yZFTPSYElqg-ZXAyTBG/view?usp=drivesdk).

## Contributing

Contributions are welcome! If you find any issues or want to enhance the live object detection system, feel free to open an issue or submit a pull request.

## Acknowledgments

- [YOLOv4](https://github.com/AlexeyAB/darknet) - You Only Look Once: Unified, Real-Time Object Detection
- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library


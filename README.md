# Eye Tracker Application

## Overview
This Python application tracks eye movements using computer vision techniques and simulates mouse clicks based on those movements. It utilizes the MediaPipe library for facial landmark detection, PyAutoGUI for mouse cursor control, Tkinter for the graphical user interface, and Pyrebase for Firebase authentication and database connectivity.

## Features
- Real-time eye tracking using a webcam
- Simulated mouse clicks triggered by blinking or closing the eyes
- Support for both left and right eye tracking
- Adjustable threshold for detecting eye closure
- User-friendly graphical user interface

## Installation
1. Clone this repository to your local machine.
   ```
   git clone <repository_url>
   ```
2. Install the required dependencies by running the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the `main.py` script to launch the application.
   ```
   python main.py
   ```
2. Position your face in front of the webcam with proper lighting conditions.
3. Follow the on-screen instructions to calibrate the eye tracking system.
4. Once calibrated, the application will track your eye movements in real-time.
5. Blink or close your eyes to simulate mouse clicks.

## Dependencies
- OpenCV
- MediaPipe
- PyAutoGUI
- Tkinter
- Pyrebase
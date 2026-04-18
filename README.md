AeroTouch AI: Intelligent Gesture Control System
Developed by: Hussein Hafez

📌 Project Overview
AeroTouch AI is a high-performance, hand-gesture control system that transforms a standard webcam into a sophisticated input device. Leveraging Computer Vision (MediaPipe) and advanced signal filtering (Kalman Filter), this tool allows for seamless desktop interaction without physical hardware.

The project is designed with stability and performance in mind, making it suitable for professional workflows, presentations, or accessibility needs.

🚀 Key Features
Precision Cursor Tracking: Uses a Kalman Filter to eliminate jitter and provide cinema-smooth mouse movement.

Multimodal Interaction: Automatically switches between 3 distinct modes:

Mouse Mode: Precision movement and "Pinch-to-Drag" selection.

Scroll Mode: Vertical scrolling using dual-finger gestures + Right-click support.

Media Mode: Real-time volume control via horizontal hand translation.

State Stability System: Implements a confirmation counter to prevent accidental clicks or mode hopping.

Low Latency: Optimized for 60 FPS performance using MediaPipe's Lite model complexity.

🛠 Tech Stack
Language: Python 3.11+

Vision: OpenCV, MediaPipe

Automation: PyAutoGUI

Mathematics: NumPy (for coordinate mapping and interpolation)

📋 Prerequisites
Ensure you have the following libraries installed:

Bash
pip install opencv-python mediapipe numpy pyautogui
🎮 How to Use
Mouse Movement: Raise only your Index Finger.

Left Click & Drag: Bring your Thumb close to your index finger while in Mouse Mode.

Scroll Mode: Raise Index and Middle fingers. Move hand up/down to scroll.

Right Click: Pinch your Index and Middle fingers together while in Scroll Mode.

Volume Control: Raise Index, Middle, and Ring fingers. Move hand Left (Decrease) or Right (Increase).

⚙️ Technical Logic
The system maps the camera coordinates (640x480) to the monitor resolution using Linear Interpolation. To ensure the user can reach the corners of the screen easily, a Safe Margin (100px) is applied to the camera feed.

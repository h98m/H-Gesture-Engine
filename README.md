# 🚀 H-Gesture-Engine
### *Master your Desktop with Air-Magic*

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Mediapipe](https://img.shields.io/badge/AI-Mediapipe-green.svg)](https://mediapipe.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenCV](https://img.shields.io/badge/Library-OpenCV-orange.svg)](https://opencv.org/)

**H-Gesture-Engine** is a high-performance, AI-driven human-computer interaction tool. It transforms a standard webcam into a sophisticated gesture-recognition sensor, allowing you to control your mouse, volume, and scrolling without touching a single piece of hardware.

---

## 🌟 Key Highlights

* **🎬 Cinematic Smoothing:** Implements a **Kalman Filter** to eliminate sensor noise and provide butter-smooth cursor movements.
* **🧠 Intelligent State Machine:** Context-aware gesture recognition that switches between Mouse, Scroll, and Media modes seamlessly.
* **⚡ Zero-Latency Logic:** Optimized for real-time performance using MediaPipe's Lite-complexity models.
* **🖱️ Virtual Drag & Drop:** Integrated "Pinch-to-Drag" logic for selecting text or moving windows.

---

## 🎮 Gestures & Controls

| Action | Hand Gesture | Mode |
| :--- | :--- | :--- |
| **Move Cursor** | ☝️ Index Finger Up | Mouse Mode |
| **Left Click / Drag** | 🤏 Index + Thumb Pinch | Selection |
| **Scroll Up/Down** | ✌️ Index + Middle Fingers | Scroll Mode |
| **Right Click** | ✂️ Pinch Index & Middle | Context Menu |
| **Volume Up/Down** | 🖐️ Three Fingers Up + Move | Media Mode |
| **App Launcher** | ✊ Fist (All fingers down) | Custom Action |

---

## 🛠️ Technical Deep Dive

The core of the engine relies on the **Kalman Filter** algorithm to predict and smooth the hand landmarks. The state of the system is estimated through:

$$\hat{x}_{k} = \hat{x}_{k-1} + G_k (z_k - \hat{x}_{k-1})$$

Where $G_k$ is the Kalman Gain, ensuring that sudden camera "glitches" or lighting changes don't cause the cursor to jump uncontrollably.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/h98m/H-Gesture-Engine.git](https://github.com/h98m/H-Gesture-Engine.git)
cd H-Gesture-Engine

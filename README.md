# Hand Gesture Controlled Robotics Car 🚗🤖

A real-time gesture controlled robotic car using computer vision.  
The system detects hand landmarks from webcam feed and sends movement commands to an Arduino via Bluetooth.

## 🛠️ Technologies Used
- Python
- OpenCV
- MediaPipe
- Serial Communication (pyserial)
- Arduino UNO + HC-05 Bluetooth Module
- L298N Motor Driver
- HC-05 Bluetooth module

## 🎮 Gesture Commands
Based on finger count detected:

| Fingers Shown | Action |
|---------------|--------|
| 👊 (0)        | Stop 🚫 |
| ☝️ (1)        | Left ⬅️ |
| ✌️ (2)        | Right ➡️ |
| ✌️☝️ (3)      | Forward ⬆️ |
| ✋ (4)        | Backward ⬇️ |

## 📁 Files in This Repo
- `HGCRC project code.py` — Main Python script  
- Demo images & videos — Visual demo of working project  
- `HGCRC project arduino code.ino` — Arduino sketch to move the robot

## 📌 How to Run
1. Clone repository  
2. Install Python packages:

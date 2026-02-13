# Hand Gesture Controlled Robotic Car 🚗🤖

This project uses Computer Vision to control a robotic car using real-time hand gestures captured from a laptop camera.

## Technologies Used
- Python
- OpenCV
- MediaPipe
- Arduino UNO
- Serial Communication
- L298N Motor Driver
- HC-05 Bluetooth Module

## Gesture Controls
- Index Finger → Left
- Two Fingers → Right
- Three Finger → Forward
- Four Fingers → Backward
- Fist → Stop

## Description
MediaPipe detects hand landmarks in real-time. Based on finger positions, commands are sent to Arduino to control the car movement.

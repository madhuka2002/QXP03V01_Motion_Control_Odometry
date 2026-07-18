# QXP03V01 – Motion Control & Odometry

![Status](https://img.shields.io/badge/Status-Completed-success)
![Platform](https://img.shields.io/badge/Platform-Webots-blue)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Robot](https://img.shields.io/badge/Robot-e--puck-orange)
![Project](https://img.shields.io/badge/Quantheonix-QXP03V01-red)

---

# Overview

**QXP03V01 – Motion Control & Odometry** is the third project in the **Quantheonix Robotics Research** roadmap.

This project focuses on developing a reusable motion control library for a differential-drive mobile robot using Python and Webots. The robot performs precise linear movement, rotational control, and continuously estimates its position using wheel encoder odometry.

Unlike previous projects that emphasized sensing and obstacle avoidance, QXP03 establishes the motion foundation required for advanced robotics topics such as navigation, localization, mapping, and SLAM.

---

# Project Information

| Property | Value |
|----------|-------|
| Project ID | QXP03V01 |
| Project Name | Motion Control & Odometry |
| Version | V01 |
| Platform | Webots |
| Robot | e-puck |
| Language | Python |
| Category | Robotics |
| Status | ✅ Completed |

---

# Objectives

- Develop accurate motion control
- Implement encoder-based odometry
- Create reusable movement functions
- Perform precise rotational control
- Build a motion library for future projects
- Establish the foundation for autonomous navigation

---

# Features

- ✅ Forward movement
- ✅ Backward movement
- ✅ Precise rotations
- ✅ Wheel encoder integration
- ✅ Continuous odometry
- ✅ Position estimation (X, Y)
- ✅ Heading estimation (θ)
- ✅ Motion primitives
- ✅ Shape trajectory execution
- ✅ Motion calibration
- ✅ Pose monitoring

---

# Technologies

- Python
- Webots
- e-puck Robot
- Differential Drive Kinematics
- Wheel Encoders
- Odometry
- Robotics Simulation

---

# Motion Primitives

The project provides reusable high-level movement commands.

```python
forward(distance)

backward(distance)

turn_left()

turn_right()

turn_around()
```

These functions abstract low-level motor control and simplify future robotics projects.

---

# Robot Capabilities

The robot can perform:

- Move Forward
- Move Backward
- Rotate Left
- Rotate Right
- Rotate 180°
- Drive Triangle
- Drive Square
- Drive Pentagon
- Drive Hexagon

---

# Odometry

The robot continuously estimates its position using wheel encoder feedback.

Estimated robot pose:

```
X Position
Y Position
Heading (θ)
```

Odometry updates occur continuously while the robot is moving.

---

# Motion Calibration

## Distance Accuracy

| Target | Measured |
|---------|----------|
| 0.50 m | 0.501 m |
| 1.00 m | 1.001 m |

Distance error remained below **0.2%**, demonstrating highly accurate linear motion.

## Rotation Accuracy

Rotation testing showed stable angular control with minor encoder-based drift, which is expected in differential-drive robots and will be addressed in future localization projects.

---

# Project Structure

```
QXP03V01_Motion_Control_Odometry/
│
├── controllers/
│   └── motion_controller/
│       └── motion_controller.py
│
├── worlds/
│   └── MotionControl.wbt
│
├── documentation/
│   ├── About.md
│   ├── README.md
│   ├── TEST_RESULTS.md
│   └── CHANGELOG.md
│
├── screenshots/
│
├── videos/
│
└── LICENSE
```

---

# Motion Workflow

```
Command

↓

Motion Controller

↓

Motor Control

↓

Wheel Encoders

↓

Odometry Update

↓

Robot Pose

(X, Y, θ)
```

---

# Testing

The motion controller was tested using:

- Forward movement
- Backward movement
- 90° rotation
- 180° rotation
- 360° rotation
- Triangle trajectory
- Square trajectory
- Pentagon trajectory
- Hexagon trajectory

All tests completed successfully.

---

# Learning Outcomes

This project demonstrates practical knowledge of:

- Differential-drive robots
- Wheel encoder processing
- Robot kinematics
- Motion control
- Continuous odometry
- Pose estimation
- Robotics software architecture
- Motion calibration
- Simulation-based robotics development

---

# Quantheonix Robotics Roadmap

```
QXP01 ✅ Radar Scanner

↓

QXP02 ✅ Obstacle Avoidance

↓

QXP03 ✅ Motion Control & Odometry

↓

QXP04 ▶ Autonomous Maze Solver

↓

QXP05 ▶ Localization

↓

QXP06 ▶ Environment Mapping

↓

QXP07 ▶ Path Planning

↓

QXP08 ▶ SLAM

↓

QXP09 ▶ Vision Navigation

↓

QXP10 ▶ AI Autonomous Robot
```

---

# Future Work

The motion library developed in this project will be reused and expanded in:

- QXP04V01 – Autonomous Maze Solver
- QXP05V01 – Robot Localization
- QXP06V01 – Environment Mapping
- QXP07V01 – Path Planning
- QXP08V01 – SLAM Fundamentals
- QXP09V01 – Vision-Based Navigation
- QXP10V01 – AI Autonomous Robot

---

# Author

**Madhu Aththanayaka**

Founder & Researcher

**Quantheonix Robotics Research**

---

# License

This project is released under the **MIT License**.

---

## Project Status

**QXP03V01 – Motion Control & Odometry**

**Status:** ✅ Completed

This project successfully establishes a reusable motion control and odometry framework for future Quantheonix autonomous robotics projects.
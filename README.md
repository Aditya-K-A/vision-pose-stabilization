# Vision-Based Pose Estimation and Stabilization System

## 🧭 Overview

This project implements a monocular, vision-only pose estimation pipeline designed for GPS-denied environments.

Given a stable reference image and a new image captured after camera movement, the system:

- Detects and matches visual features  
- Estimates relative camera motion  
- Extracts planar movement components (ΔX, ΔY, Δθ)  
- Computes corrective motion to return to the original pose  

This forms the foundation of a vision-based stabilization system suitable for drones and robotics.

---

## Requirements

- Python 3.8+
- OpenCV
- NumPy

All dependencies are listed in `requirements.txt`.

---

## 📍 Problem Definition

Design a vision-only system that:

- Accepts a reference frame  
- Accepts a current frame  
- Detects feature correspondences  
- Estimates camera motion:
  - Left / Right shift (ΔX)
  - Up / Down shift (ΔY)
  - Rotation (Δθ)
- Computes corrective motion to return to the reference pose  

The system operates without GPS and relies purely on visual information.

---

## ⚙️ System Pipeline

1. ORB Feature Detection  
2. Descriptor Matching (Brute-Force Matcher)  
3. Outlier Rejection using RANSAC  
4. Essential Matrix Estimation  
5. Pose Recovery (R, t)  
6. Planar Motion Extraction (ΔX, ΔY, Δθ)  
7. Corrective Motion Computation  
8. Visualization of Results  

Corrective motion is computed as:

    Correction = - Estimated Motion

This suggests the necessary movement to return to the original pose.


---

## Key Features

- Monocular visual odometry  
- Robust feature-based matching  
- RANSAC-based outlier filtering  
- Planar motion extraction  
- Drift correction computation  
- Visualization of inlier matches and motion direction  
- CPU-friendly (no GPU required)  

---

## How to Run

1. Update image paths inside `src/main.py`
2. Run: python src/main.py


Output images and motion estimates are saved in the `results/` directory.

---

## Assumptions

- Monocular camera setup  
- Approximated camera intrinsics  
- Sufficient scene texture  
- Small inter-frame motion  
- Mostly planar indoor environment  

---

## Limitations

- Translation scale is up-to-scale (monocular ambiguity)  
- Performance degrades in low-texture environments  
- Assumes planar motion (not full 6DoF extraction)  
- Sensitive to motion blur  

---

## 🚀 Conclusion

This implementation demonstrates a complete feature-based pose estimation pipeline capable of estimating relative motion and generating corrective commands in GPS-denied environments.  
The system is modular, lightweight, and can be extended toward full 6DoF visual odometry or real-time drone stabilization.



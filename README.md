# 🎨 Pseudo-3D Image Augmentation App

**English** | [日本語版 (Japanese)](./README_JA.md)

> **A Universal Pseudo-3D Volumetric Pseudo-Geometry Modeling & Automated Rotation-Augmented Annotation App with Auto-Generated YOLO data.yaml**

[![HTML5 / WebGL](https://img.shields.io/badge/Tech-WebGL%2FThree.js-blue.svg)](https://threejs.org/)
[![OpenCV](https://img.shields.io/badge/Backend-OpenCV%20Python-green.svg)](https://opencv.org/)
[![YOLO Support](https://img.shields.io/badge/Dataset-YOLO%20Format%20%2B%20data.yaml-orange.svg)](https://docs.ultralytics.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](#license)

---

## 📌 Overview

**Pseudo-3D Image Augmentation App** is a universal web-based computer vision tool designed to synthesize multi-angle, 3D-rotated training datasets from a single 2D input photo. 

By applying a **5-point multi-node volumetric pseudo-geometry deformation engine**, the application reconstructs plausible 3D curvature and volumetric depth from flat 2D images (organisms, mechanical components, industrial parts, vehicles, animals, etc.). It automates full 3-axis rotation modulation (Yaw, Pitch, Roll) at 1.0° intervals, generates high-precision YOLO annotations, and exports a complete training dataset with an automatically structured `data.yaml` config file.

---

## 🔬 Background & Resolving Angle-Bias in Object Detection

In deep learning object detection models (such as YOLOv8, YOLOv9, YOLOv10, YOLOv11), datasets collected from real-world sensors (ROVs, satellites, single-view cameras) often suffer from **severe angle bias** due to an overrepresentation of frontal-view photographs. This causes a dramatic drop in detection accuracy when objects appear at tilted or side-profile angles.

Rather than requiring costly physical multi-view re-shooting, **Pseudo-3D Image Augmentation App** augments single-angle photographs into thousands of synthetic multi-view training samples, significantly boosting AI model generalization performance across all viewing perspectives.

---

## 🌟 Key Features

### 1. 🏷️ Custom YOLO Class Specification (Class ID & Class Name UI)
* Configure **`YOLO Class ID`** (e.g., `0`, `1`, `2`) and **`Class Name`** (e.g., `car`, `jellyfish`, `component`) directly from the sidebar UI.
* Drag-and-drop any custom image or target object; the specified class labels are dynamically embedded into the generated bounding box annotations.

### 2. 📄 Auto-Generated YOLO `data.yaml` & One-Click ZIP Export
* Exporting the dataset automatically generates the standard Ultralytics YOLO dataset configuration file (`data.yaml`) alongside images (`/images/`) and labels (`/labels/`).

```yaml
# Pseudo-3D Image Augmentation App Generated YOLO Dataset Config
path: ./
train: images
val: images

names:
  0: "jellyfish"
```
* Simply unzip and feed directly into YOLO training pipelines without manual configuration.

### 3. 🖼️ Two-Layer Composition (RGBA Foreground + CV2 Inpainted Background)
* Uses OpenCV's Telea algorithm (`cv2.inpaint`) to seamlessly repair and fill the background behind the target object.
* Extracts the target as a 4-channel RGBA transparent texture, rendering it over the inpainted background layer (`Z = -0.01` and `Z = 0`) in Three.js WebGL space.

### 4. 🌸 5-Point Multi-Node Volumetric Deformation Engine
* Independently control the apex height (`Dome Depth`), outer shoulder depths (`Shoulders`), distribution radius (`Radius`), and peak offsets (`Apex Shift`).
* Applies Gaussian volumetric warping to flat photos, creating natural 3D curvature and realistic silhouettes under rotation.

### 5. 🤖 Automated 3D Batch Capture (Yaw / Pitch / Roll Modulation)
* **`🚀 20-Frame Automated Yaw Capture (ΔYaw=+1.0°)` [Shortcut: `Y`]**
* **`🚀 20-Frame Automated Pitch Capture (ΔPitch=+1.0°)` [Shortcut: `P`]**
* **`🚀 20-Frame Automated Roll Capture (ΔRoll=+1.0°)` [Shortcut: `R`]**
* **`🌀 Custom Multi-Axis Batch Capture` [Shortcut: `Shift + A`]**: Configure 1 to 50 frames with custom multi-axis angle increments.

### 6. 📐 3D Rotation-Driven Auto-Scaling BBox Model
* Dynamically scales bounding box margins during 3D rotations—expanding near-side boundaries and shrinking far-side boundaries to fit perspective depth changes. Includes scale sensitivity adjustments (`0.0x` to `3.0x`).

### 7. 🔴 Real-Time Red BBox Projection & CVAT-Style Drag-Correction
* Projects real-time red bounding box overlays (`#ef4444`) onto the 3D canvas with live Class ID and Class Name indicators.
* Interactive edge lines and corner handles allow intuitive CVAT-style manual adjustments.

### 8. 📦 Interactive Capture Log Gallery, Hover Preview Modal & One-Click Trash [✕]
* Review captured frames in a collapsible sidebar gallery.
* Hovering over thumbnails opens a high-resolution preview modal with red BBox overlays and raw YOLO label coordinates.
* Instantly delete unwanted/out-of-bounds frames using the **`[✕]` button** or **Keyboard Shortcuts (`[X]` / `[Delete]`)**.

---

## ⌨️ Keyboard Shortcuts

| Shortcut Key | Action |
| :--- | :--- |
| **`[C]`** | 📸 Capture single frame (1.1x Cropped Image + YOLO `.txt`) |
| **`[Y]`** | 🚀 Run 20-Frame Automated Yaw Batch Capture (ΔYaw = +1.0°) |
| **`[P]`** | 🚀 Run 20-Frame Automated Pitch Batch Capture (ΔPitch = +1.0°) |
| **`[R]`** | 🚀 Run 20-Frame Automated Roll Batch Capture (ΔRoll = +1.0°) |
| **`[Shift + A]`** | 🌀 Run Custom Multi-Axis Automated Batch Capture |
| **`[X]` / `[Delete]`** | 🗑️ Delete hovered or latest capture log entry |

---

## 🛠️ Standalone Architecture & Python Build Engine

The application is completely standalone and runs directly in modern web browsers (Chrome, Safari, Firefox, Edge) without requiring a backend server or internet connection.

### Directory Structure
```text
Github/
├── pseudo_3d_image_augmentation_app.html  # Main Application (Standalone HTML)
├── build_3d_tool.py                       # Automated Python Build Script
├── README.md                              # English Documentation
└── README_JA.md                           # Japanese Documentation
```

### Python Re-Build Engine (`build_3d_tool.py`)
To package custom default image datasets into the standalone HTML file, run the automated Python build script:

```bash
pip install opencv-python numpy
python build_3d_tool.py
```

---

## 🚀 Quick Start Guide

1. **Launch App**: Open `pseudo_3d_image_augmentation_app.html` in any web browser.
2. **Set Class & Input Image**: Enter your `Class ID` and `Class Name` in the sidebar, then drop your image into the drop zone.
3. **Deform & Augment**: Adjust 3D volumetric depth sliders and run automated batch captures (`[Y]`, `[P]`, `[R]`).
4. **Export Dataset**: Click **`📦 Export Dataset (ZIP)`** to download your complete YOLO dataset containing `/images/`, `/labels/`, and `data.yaml`.

---

## 📝 Citation

If you use this application or dataset augmentation workflow in your research or commercial projects, please cite:

```bibtex
@misc{pseudo_3d_image_augmentation_app_2026,
  author = {Kei Nagaoka},
  title = {Pseudo-3D Image Augmentation App: A Universal Pseudo-3D Volumetric Pseudo-Geometry Modeling & Automated Rotation-Augmented Annotation App with Auto-Generated YOLO data.yaml},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/your-username/Pseudo-3D-Image-Augmentation-App}}
}
```

---

## 📜 License

Distributed under the MIT License.

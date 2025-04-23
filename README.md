# 🗑️ TrashDnC-YOLOv8: Waste Detection with YOLOv8

This repository contains the training scripts, configuration, and trained YOLOv8 model for detecting and classifying different types of waste using a modified version of the TACO dataset.

## 📦 Project Structure

## 🧠 Classes

This model detects and classifies waste into 6 broad categories:
- `plastic`
- `metal`
- `glass`
- `paper`
- `other`
- `unknown`

> **Note:** "Unknown" is reserved for unidentifiable or unlabeled trash.

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/TrashDnC-YOLOv8.git
cd TrashDnC-YOLOv8
```

2. Set Up Environment
Create a virtual environment and install dependencies:

```
pip install -r requirements.txt
```

Or manually install YOLOv8:
```
pip install ultralytics
```

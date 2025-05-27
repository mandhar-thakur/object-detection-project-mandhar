# YOLOv8 Rock-Paper-Scissors Object Detection

This project uses **YOLOv8** to detect hand gestures: **Rock, Paper, and Scissors** using a custom-trained model.  
Built as part of an AI internship project, this repository contains:

- Trained model weights (`best.pt`)
- Streamlit interface (`app.py`)
- Project report
- Instructions to run and test it

---

## 🧠 Model Details

Architecture: YOLOv8-nano (anchor-free, CNN-based)  
CNN Model Used - Default YOLOv8 - C2f Model  
Classes: Rock, Paper, Scissors  
Training Epochs: 15  
Trained on: Roboflow dataset, version 14  
Accuracy: ~91% mAP@0.5

---

## 📁 Files Included

| File/Folders         | Description                          |
|----------------------|--------------------------------------|
| `app.py`             | Streamlit web app to test the model  |
| `best.pt`            | Trained YOLOv8 model                 |
| `requirements.txt`   | Python dependencies                  |
| `YOLOv8_Report.docx` | Internship project report            |

---

## 🧪 How to Install and Run

### 1. Install dependencies:
bash
pip install -r requirements.txt

### 2. Run the Streamlit App:
streamlit run app.py

## 📦 Dataset
The dataset was not uploaded to GitHub due to size. You can automatically download it from Roboflow using the following code:

!pip install roboflow
from roboflow import Roboflow

rf = Roboflow(api_key="your_api")
project = rf.workspace("your-workspace").project("rock-paper-scissors-sxsw")
dataset = project.version(14).download("yolov8")

Or visit the Roboflow project:
Dataset Link - https://universe.roboflow.com/ds/wxXW2AEbJF?key=m0tZdm2zi5

## 📸 Sample Results
![image](https://github.com/user-attachments/assets/8843a6d8-ef38-41a8-a8b7-8ab20ba9f6c3)

![image](https://github.com/user-attachments/assets/84f5be27-d9ca-4303-af80-3c296c149bda)


## 📈 Future Scope
Add webcam-based live detection

Export to ONNX for mobile/web deployment

Train longer with more data (20–50 epochs)

Try EfficientNet or MobileNet backbones

## ✍️ Author
Mandhar
📅 May 2025

## 🙌 Special Thanks
Ultralytics for YOLOv8

Roboflow for dataset hosting

Streamlit for app UI framework





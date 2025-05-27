import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

model = YOLO("/content/runs/detect/train2/weights/best.pt")

st.title("🧠 Rock-Paper-Scissors Detector (YOLOv8)")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    results = model.predict(image, conf=0.25)
    output = results[0].plot()
    st.image(np.array(output), caption="Prediction", use_column_width=True)

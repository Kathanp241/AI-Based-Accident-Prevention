import streamlit as st
import cv2
from ultralytics import YOLO
from utils import is_in_danger_zone, log_event

st.title("🛡️ AI-Based Safety Monitor")

model = YOLO("yolov8n.pt")
CONF_THRESHOLD = 0.5
DANGER_ZONE = (100, 100, 400, 300)

run = st.checkbox("Start Monitoring")
FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not detected")
            break

        # (Detection and annotation code same as main.py)
        # Convert BGR to RGB and display
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if st.button("Stop"):
            break

    cap.release()

import streamlit as st
import cv2

st.title("Camera Snapshot Test")

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

if not ret:
    st.error("Camera not detected. Try a different index or check permissions.")
else:
    st.image(frame, caption="Camera Snapshot")

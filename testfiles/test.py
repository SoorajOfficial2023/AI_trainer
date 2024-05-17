import streamlit as st
import cv2
from PIL import Image
import numpy as np

def main():
    st.title("Webcam Live Stream")
    
    run = st.checkbox('Run')
    
    FRAME_WINDOW = st.image([])
    
    if run:
        video_url = "http://192.168.29.115:8501"  # Replace this with your network stream URL
        video_capture = cv2.VideoCapture(video_url)
        if not video_capture.isOpened():
            st.error("Failed to open network stream. Please check the URL and try again.")
            return

        while run:
            ret, frame = video_capture.read()
            if not ret:
                st.error("Failed to capture frame from network stream.")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
        video_capture.release()

if __name__ == '__main__':
    main()

import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tempfile

st.title("Webcam Capture & Save App")

# Browser camera input
picture = st.camera_input("Take a picture")

if picture:
    # Convert to OpenCV format
    image = Image.open(picture)
    img_array = np.array(image)

    st.image(img_array, caption="Captured Image")

    # Save image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
    cv2.imwrite(temp_file.name, cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))

    st.success("Image Saved Successfully!")
    st.download_button(
        label="Download Image",
        data=open(temp_file.name, "rb"),
        file_name="captured_image.jpg"
    )

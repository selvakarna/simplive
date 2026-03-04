import streamlit as st
from PIL import Image
import numpy as np
import cv2
from rembg import remove
import tempfile

st.title("Live Camera - Background Remove Option")

# Camera input (browser based)
picture = st.camera_input("Take a picture")

if picture:
    image = Image.open(picture)
    img_array = np.array(image)

    col1, col2 = st.columns(2)

    with col1:
        remove_bg = st.button("Remove Background")

    with col2:
        keep_original = st.button("Keep Original")

    if remove_bg:
        # Remove background using AI
        output = remove(image)
        output_np = np.array(output)

        st.image(output_np, caption="Background Removed")

        # Save
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
        cv2.imwrite(
            temp_file.name,
            cv2.cvtColor(output_np, cv2.COLOR_RGBA2BGRA),
        )

        st.download_button(
            "Download Image",
            data=open(temp_file.name, "rb"),
            file_name="bg_removed.png",
        )

    if keep_original:
        st.image(img_array, caption="Original Image")

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        cv2.imwrite(
            temp_file.name,
            cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR),
        )

        st.download_button(
            "Download Image",
            data=open(temp_file.name, "rb"),
            file_name="original.jpg",
        )

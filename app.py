import streamlit as st
from PIL import Image
import numpy as np
import cv2
from streamlit_drawable_canvas import st_canvas
import tempfile

st.title("Live Camera - Manual Background Removal")

# Capture from browser camera
picture = st.camera_input("Take a picture")

if picture:
    image = Image.open(picture)
    img_array = np.array(image)

    st.subheader("Step 1: Use Mouse to Remove Background")

    # Drawable canvas
    canvas_result = st_canvas(
        fill_color="rgba(0, 0, 0, 1)",  # Erase area
        stroke_width=20,
        stroke_color="black",
        background_image=image,
        update_streamlit=True,
        height=image.size[1],
        width=image.size[0],
        drawing_mode="freedraw",
        key="canvas",
    )

    if canvas_result.image_data is not None:
        # Convert canvas to numpy
        edited_image = canvas_result.image_data.astype(np.uint8)

        st.subheader("Processed Image")
        st.image(edited_image)

        # Save button
        if st.button("Save Image"):
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
            cv2.imwrite(
                temp_file.name,
                cv2.cvtColor(edited_image, cv2.COLOR_RGBA2BGR),
            )

            st.success("Image Saved!")
            st.download_button(
                "Download Image",
                data=open(temp_file.name, "rb"),
                file_name="bg_removed.png",
            )

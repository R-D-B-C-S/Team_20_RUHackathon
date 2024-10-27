import streamlit as st
import pandas as pd
import os
from PIL import Image
from datetime import datetime
import time
now = str(datetime.now())
header = st.container()


with header:
    st.title("Sonogram image uploader")
    st.text("Please upload your Sonogram below")

df = st.file_uploader(label = "Upload Home Sonogram:",type=["jpg", "jpeg", "png"])

save_directory = "uploaded_images"

# Create the directory if it does not exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

if df is not None:
    # Open the uploaded image using PIL
    image = Image.open(df)

    st.image(image, caption='Uploaded Image', use_column_width=True)

    save_path = os.path.join(save_directory, df.name)

    with open(save_path, "wb") as f:
        f.write(df.getbuffer())

    progress_bar = st.progress(0)
    for completion in range(100):
        time.sleep(0.02)
        progress_bar.progress(completion+1)


    st.success(f"Image successfully saved to {save_path}")
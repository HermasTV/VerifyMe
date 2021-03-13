import requests
import streamlit as st
from PIL import Image

def app(result=None):

    st.set_option("deprecation.showfileUploaderEncoding", False)

    # defines an h1 header
    st.title("ID OCR System")

    # displays a file uploader widget
    id_img = st.file_uploader("Choose ID image")

    if st.button("ocr"):
        if id_img is not None:
            files = {"id": id_img.getvalue()}
            #res = requests.post(f"http://api:8000/match", files=files)
            res = requests.post(f"http://localhost:8000/ocr", files=files)
            res = res.json()
            st.write(res)

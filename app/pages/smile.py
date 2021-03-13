import requests
import streamlit as st
from PIL import Image

def app(result=None):

    st.set_option("deprecation.showfileUploaderEncoding", False)

    # defines an h1 header
    st.title("Smile recognition")

    # displays a file uploader widget
    img = st.file_uploader("upload a selfie with a smile")

    if st.button("detect"):
        if img is not None:
            files = {"img": img.getvalue()}
            #res = requests.post(f"http://api:8000/match", files=files) #for the docker version
            res = requests.post(f"http://localhost:8000/action", files=files)
            res = res.json()
            st.write(res)
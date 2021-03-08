import requests
import streamlit as st
from PIL import Image

# https://discuss.streamlit.io/t/version-0-64-0-deprecation-warning-for-st-file-uploader-decoding/4465
st.set_option("deprecation.showfileUploaderEncoding", False)

# defines an h1 header
st.title("face Matching app ")

# displays a file uploader widget
img1 = st.file_uploader("Choose ID image")
img2 = st.file_uploader("Choose selfie Image")

#fffff
# displays a button
if st.button("match"):
    if img1 is not None and img2 is not None:
        files = {"id": img1.getvalue(),
                 "selfie":img2.getvalue()}
        res = requests.post(f"http://api:8000/match", files=files)
        res = res.json()
        result = res['result']
        st.text(result)
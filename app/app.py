import requests
import streamlit as st
from pages import match,ocr,smile
from streamlit import caching



# create your radio button with the index that we loaded
choice = st.sidebar.radio("go to",('home','ocr', 'match', 'action'))

# finally get to whats on each page
if choice == 'home':
    st.write("Home Page")
elif choice == 'ocr':
    ocr.app()
elif choice == 'match':
    match.app()
elif choice == 'action':
    smile.app()
    st.write("Action Page")

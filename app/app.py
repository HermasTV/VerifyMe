import requests
import streamlit as st
from streamlit import caching


from pages import match,ocr,smile,generate,users


# create your radio button with the index that we loaded
choice = st.sidebar.radio("go to",('home','ocr', 'match', 'action','users'))

# finally get to whats on each page
if choice == 'home':

    st.write("Home Page")
    generate.app()
elif choice == 'ocr':
    ocr.app()
elif choice == 'match':
    match.app()
elif choice == 'action':
    smile.app()
    st.write("Action Page")
elif choice == 'users':
    users.app()



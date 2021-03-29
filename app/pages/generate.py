import requests
import streamlit as st

def app():

    username = st.text_input("Enter Your User Name","username")
    email = st.text_input("Enter Your Email address","email")
    if st.button("Generate Token"):
            
            req={
                'username':username,
                'email':email,
                'connectDB':True}
            
            res = requests.post(f"http://api:8000/generate",data=req)
            token = res.json()
            st.write(token)
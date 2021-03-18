import requests
import streamlit as st

def app():

    username = st.text_input("Enter Your User Name","username")
    email = st.text_input("Enter Your Email address","email")
    if st.button("Generate Token"):
            
            req={
                'username':username,
                'email':email}
            
            res = requests.post(f"http://localhost:8000/generate",data=req)
            res = res.json()
            token = res['token']
            print(token)
            st.write(token)
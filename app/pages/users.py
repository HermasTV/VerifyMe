import requests
import streamlit as st
import pandas as pd
import json

def app():

    response = requests.get(f"http://api:8000/users")
    df = pd.DataFrame(json.loads(response.text))
    st.dataframe(df)
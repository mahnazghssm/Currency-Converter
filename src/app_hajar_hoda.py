import streamlit as st
from test import response 
st.title(":dollar: Currency Converter")
st.markdown(""" This tool allows you to instantly converter amounts between different currencies. Enter the amount and choose the currencies to see the result.""")
url = f"https: //api.exchangerate-api.com/v4/latest/USD"
import requests
response = requests.get(url)
list response.json(["rates"].keys())
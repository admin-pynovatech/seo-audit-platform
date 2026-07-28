import streamlit as st

from utils.validators import validate_url

st.title("Website Audit")

url = st.text_input("Enter Website URL")

if st.button("Validate"):

    if validate_url(url):
        st.success("Valid URL")

    else:
        st.error("Invalid URL")
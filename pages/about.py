import streamlit as st

from config import Config

st.title("ℹ️ About")

st.markdown(
    f"""
    ### {Config.APP_NAME}

    Version: **{Config.APP_VERSION}**

    A modern SEO auditing platform developed with Python and Streamlit.

    Maintained by **PyNova Tech**.
    """
    )
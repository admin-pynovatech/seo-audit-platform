"""
Application entry point.

Configures the Streamlit application and registers
all pages for navigation.
"""

import streamlit as st

from config import Config


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title=Config.APP_NAME,
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==========================================
# Application Pages
# ==========================================

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊",
)

website_crawler = st.Page(
    "pages/website_crawler.py",
    title="Website Crawler",
    icon="🌐",
)

about = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️",
)


# ==========================================
# Navigation
# ==========================================

navigation = st.navigation(
    {
        "Website Crawler Platform": [
            dashboard,
            website_crawler,
            about,
        ]
    }
)

navigation.run()
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Website Crawler",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Pages
# --------------------------------------------------
dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊"
)

website_audit = st.Page(
    "pages/website_audit.py",
    title="Website Crawler",
    icon="🌐"
)

about = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️"
)

# --------------------------------------------------
# Navigation
# --------------------------------------------------
pg = st.navigation(
    {
        "Website Crawler Platform": [
            dashboard,
            website_audit,
            about
        ]
    }
)

pg.run()
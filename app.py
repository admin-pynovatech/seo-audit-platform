import streamlit as st

from config import Config

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT,
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🔍 SEO Audit Platform")
st.sidebar.markdown(f"**Version:** {Config.APP_VERSION}")
st.sidebar.divider()

# ---------------------------------------------------
# Navigation
# ---------------------------------------------------
dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
    icon="📊",
)

website_audit = st.Page(
    "pages/website_audit.py",
    title="Website Audit",
    icon="🌐",
)

reports = st.Page(
    "pages/reports.py",
    title="Reports",
    icon="📄",
)

about = st.Page(
    "pages/about.py",
    title="About",
    icon="ℹ️",
)

navigation = st.navigation(
    [
        dashboard,
        website_audit,
        reports,
        about,
    ]
)

navigation.run()
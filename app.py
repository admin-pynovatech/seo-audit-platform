import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="SEO Audit Platform",
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
    title="Website Audit",
    icon="🌐"
)

reports = st.Page(
    "pages/reports.py",
    title="Reports",
    icon="📄"
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
        "SEO Audit Platform": [
            dashboard,
            website_audit,
            reports,
            about
        ]
    }
)

pg.run()
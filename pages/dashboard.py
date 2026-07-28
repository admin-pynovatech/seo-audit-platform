import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Website Crawler Dashboard")

st.markdown("""
Welcome to the **Website Crawler** application.

This tool allows you to crawl a website, inspect HTTP responses, and analyze
basic webpage information through an interactive dashboard.

Use the navigation menu on the left to start crawling websites.
""")

st.divider()

# -----------------------------------
# Quick Overview
# -----------------------------------

st.subheader("🚀 Quick Overview")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.metric("Project", "Website Crawler")
        st.caption("Python & Streamlit")

with col2:
    with st.container(border=True):
        st.metric("Version", "1.0.0")
        st.caption("Demo Release")

with col3:
    with st.container(border=True):
        st.metric("Status", "Ready")
        st.caption("Start Crawling")

# -----------------------------------
# Features
# -----------------------------------

st.divider()

st.subheader("✨ Features")

features = [
    "🌐 Website URL Validation",
    "🚀 Website Crawling",
    "📡 HTTP Request & Response Analysis",
    "⏱️ Response Time Measurement",
    "🔄 Redirect Detection",
    "📄 Page Title Extraction",
    "🖥️ Server Information",
    "📦 Content Type & Encoding Detection",
    "📊 Page Statistics",
    "📑 HTTP Headers Viewer",
]

for feature in features:
    st.markdown(f"- {feature}")

# -----------------------------------
# Workflow
# -----------------------------------

st.divider()

st.subheader("⚙️ Workflow")

st.code("""
Enter Website URL
        │
        ▼
Validate URL
        │
        ▼
Send HTTP Request
        │
        ▼
Download HTML
        │
        ▼
Extract Website Information
        │
        ▼
Display Crawl Results
""", language="text")

# -----------------------------------
# Technology Stack
# -----------------------------------

st.divider()

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.info("🐍 Python")

with tech2:
    st.info("🎈 Streamlit")

with tech3:
    st.info("🌐 Requests")

with tech4:
    st.info("🍲 BeautifulSoup4")

# -----------------------------------
# Get Started
# -----------------------------------

st.divider()

st.success(
    "👈 Select **Website Crawler** from the sidebar to begin crawling a website."
)
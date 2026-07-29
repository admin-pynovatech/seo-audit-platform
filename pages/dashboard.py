"""
Dashboard page for the Website Crawler application.
"""

import streamlit as st

from config import Config


st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Website Crawler Dashboard")

st.markdown(
    f"""
Welcome to **{Config.APP_NAME}**.

This application demonstrates the fundamentals of **web crawling**, **HTTP communication**, and **HTML parsing** using Python.

Use the navigation menu to crawl websites, inspect HTTP responses, and explore webpage information through an interactive dashboard.
"""
)

st.divider()

# ==========================================
# Quick Overview
# ==========================================

st.subheader("🚀 Quick Overview")

overview = [
    ("Project", Config.APP_NAME, "Python & Streamlit"),
    ("Version", Config.APP_VERSION, "Current Release"),
    ("Status", "Ready", "Start Crawling"),
]

columns = st.columns(len(overview))

for column, (title, value, caption) in zip(columns, overview):
    with column:
        with st.container(border=True):
            st.metric(title, value)
            st.caption(caption)

# ==========================================
# Features
# ==========================================

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
    "📦 Content Type Detection",
    "🔤 Character Encoding Detection",
    "📏 Content Length Information",
    "📊 Page Statistics",
    "📑 HTTP Response Headers Viewer",
]

left_column, right_column = st.columns(2)

half = len(features) // 2

with left_column:
    for feature in features[:half]:
        st.markdown(f"- {feature}")

with right_column:
    for feature in features[half:]:
        st.markdown(f"- {feature}")

# ==========================================
# Workflow
# ==========================================

st.divider()

st.subheader("⚙️ Workflow")

st.code(
    """
Enter Website URL
        │
        ▼
Validate URL
        │
        ▼
Send HTTP Request
        │
        ▼
Download Webpage HTML
        │
        ▼
Extract Website Information
        │
        ▼
Display Crawl Results
""",
    language="text",
)

# ==========================================
# Technology Stack
# ==========================================

st.divider()

st.subheader("🛠️ Technology Stack")

technologies = [
    "🐍 Python",
    "🎈 Streamlit",
    "🌐 Requests",
    "🍲 BeautifulSoup4",
]

columns = st.columns(len(technologies))

for column, technology in zip(columns, technologies):
    with column:
        st.info(technology)

# ==========================================
# Get Started
# ==========================================

st.divider()

st.success(
    "👈 Select **Website Crawler** from the sidebar to begin exploring a website."
)
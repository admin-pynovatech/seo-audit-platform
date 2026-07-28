import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Website Crawler")

st.markdown("""
## Overview

**Website Crawler** is a Python-based web crawling application built with
**Streamlit** that allows users to inspect websites by sending HTTP requests,
retrieving webpage information, and displaying useful crawling statistics.

The application is designed to demonstrate the fundamentals of web crawling,
HTTP communication, HTML parsing, and interactive dashboard development using Python.
""")

st.divider()

st.subheader("✨ Features")

features = [
    "Website URL Validation",
    "Website Crawling",
    "HTTP Request & Response Analysis",
    "Response Time Measurement",
    "Redirect Detection",
    "Page Title Extraction",
    "Server Information",
    "Content Type Detection",
    "Character Encoding Detection",
    "Content Length Information",
    "Page Statistics",
    "HTTP Headers Viewer",
]

for feature in features:
    st.markdown(f"✅ {feature}")

st.divider()

st.subheader("🛠️ Technology Stack")

tech_stack = [
    "Python",
    "Streamlit",
    "Requests",
    "BeautifulSoup4",
    "Pandas",
    "Python-dotenv",
]

for tech in tech_stack:
    st.markdown(f"- {tech}")

st.divider()

st.subheader("📁 Project Structure")

st.code("""
website-crawler/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── dashboard.py
│   ├── website_crawler.py
│   └── about.py
│
├── services/
│   └── crawler.py
│
├── utils/
│   ├── helpers.py
│   └── validators.py
│
└── assets/
""", language="text")

st.divider()

st.subheader("🎯 Project Goals")

st.markdown("""
This project aims to:

- Learn the fundamentals of web crawling.
- Understand HTTP requests and responses.
- Parse HTML using BeautifulSoup.
- Build interactive dashboards with Streamlit.
- Develop clean, modular Python applications following best practices.
""")

st.divider()

st.subheader("🚀 Future Improvements")

future_features = [
    "robots.txt Detection",
    "sitemap.xml Detection",
    "HTML Language Detection",
    "Charset Detection",
    "Favicon Detection",
    "Forms & Buttons Counter",
    "Video & Audio Detection",
    "Cookie Analysis",
    "Security Headers Inspection",
    "Asynchronous Crawling using asyncio",
    "FastAPI REST API",
    "Docker Support",
]

for item in future_features:
    st.markdown(f"🔹 {item}")

st.divider()

st.subheader("👨‍💻 Developed By")

st.markdown("""
**PyNova Tech**

Building practical Python, AI, Automation, and Data Analytics solutions.

**GitHub:** https://github.com/admin-pynovatech
""")

st.divider()

st.caption("Website Crawler • Version 1.0.0")
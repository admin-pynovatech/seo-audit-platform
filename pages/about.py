import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About SEO Audit Platform")

st.markdown("""
## Overview

SEO Audit Platform is a Streamlit-based application that analyzes a website's
technical SEO and provides actionable insights to improve search engine visibility.
""")

st.divider()

st.subheader("Features")

features = [
    "Website Crawling",
    "Technical SEO Analysis",
    "Broken Link Detection",
    "Google PageSpeed Insights",
    "Report Generation",
]

for feature in features:
    st.markdown(f"✅ {feature}")

st.divider()

st.subheader("Technology Stack")

tech_stack = [
    "Python",
    "Streamlit",
    "BeautifulSoup",
    "Requests",
    "ReportLab",
    "Google PageSpeed Insights API",
]

for tech in tech_stack:
    st.markdown(f"- {tech}")

st.divider()

st.subheader("Project Structure")

st.code("""
seo-audit-platform/
│
├── pages/
├── services/
├── utils/
├── reports/
├── assets/
├── app.py
└── config.py
""", language="text")

st.divider()

st.caption("Version 1.0.0")
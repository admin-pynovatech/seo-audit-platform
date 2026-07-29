"""
About page for the Website Crawler application.
"""

import streamlit as st

from config import Config


st.title("ℹ️ About Website Crawler")

st.markdown(
    f"""
**{Config.APP_NAME}** is a lightweight web crawling application built with
**Python**, **Streamlit**, **Requests**, and **BeautifulSoup**.

The project demonstrates how to send HTTP requests, parse HTML documents,
extract webpage information, and present the results through an interactive
dashboard.
"""
)

st.divider()

# ==========================================
# Project Overview
# ==========================================

st.subheader("📌 Project Overview")

st.markdown(
    """
This application allows users to:

- Validate website URLs
- Crawl webpages
- Analyze HTTP responses
- Extract webpage metadata
- View page statistics
- Inspect HTTP response headers

The project is intended as a practical example of modern Python application
development using a clean and modular architecture.
"""
)

# ==========================================
# Technology Stack
# ==========================================

st.divider()

st.subheader("🛠️ Technology Stack")

technologies = [
    ("🐍 Python", "Core Programming Language"),
    ("🎈 Streamlit", "Interactive Web Interface"),
    ("🌐 Requests", "HTTP Client"),
    ("🍲 BeautifulSoup4", "HTML Parsing"),
    ("🐼 Pandas", "Data Presentation"),
    ("⚙️ Python-dotenv", "Environment Configuration"),
]

for technology, description in technologies:
    with st.container(border=True):
        st.write(f"**{technology}**")
        st.caption(description)

# ==========================================
# Project Structure
# ==========================================

st.divider()

st.subheader("📁 Project Structure")

st.code(
    """
website-crawler/
│
├── app.py
├── config.py
├── pages/
├── services/
├── utils/
├── assets/
└── screenshots/
""",
    language="text",
)

# ==========================================
# Skills Demonstrated
# ==========================================

st.divider()

st.subheader("🚀 Skills Demonstrated")

skills = [
    "Python Development",
    "HTTP Communication",
    "Web Crawling",
    "HTML Parsing",
    "Data Extraction",
    "Streamlit Development",
    "Project Architecture",
    "Configuration Management",
    "Error Handling",
]

left_column, right_column = st.columns(2)

half = len(skills) // 2

with left_column:
    for skill in skills[:half]:
        st.markdown(f"- {skill}")

with right_column:
    for skill in skills[half:]:
        st.markdown(f"- {skill}")

# ==========================================
# Future Improvements
# ==========================================

st.divider()

st.subheader("🎯 Future Improvements")

future = [
    "robots.txt Detection",
    "sitemap.xml Detection",
    "HTML Language Detection",
    "Favicon Detection",
    "Cookie Analysis",
    "Security Header Inspection",
    "Multi-page Crawling",
    "Async Crawling using asyncio",
    "FastAPI REST API",
    "Docker Support",
]

for item in future:
    st.markdown(f"- {item}")

# ==========================================
# About PyNova Tech
# ==========================================

st.divider()

st.subheader("👨‍💻 About PyNova Tech")

st.markdown(
    """
PyNova Tech develops practical software solutions using modern Python
technologies.

Areas of expertise include:

- 🤖 Artificial Intelligence
- 🧠 Agentic AI
- 📊 Data Analytics
- 🐍 Python Development
- ⚙️ Workflow Automation
- 🌐 Web Applications
- 🔌 FastAPI Development

This repository is part of a growing portfolio showcasing practical,
production-inspired Python applications.
"""
)

st.info(
    "⭐ If you found this project useful, consider starring the repository on GitHub."
)

st.caption(f"{Config.APP_NAME} • Version {Config.APP_VERSION}")
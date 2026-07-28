import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 SEO Audit Dashboard")

st.markdown(
    """
Welcome to the **SEO Audit Platform**.

Use the sidebar to navigate through the application.
"""
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Audits",
        "0"
    )

with col2:
    st.metric(
        "Average SEO Score",
        "0"
    )

with col3:
    st.metric(
        "Broken Links",
        "0"
    )

st.divider()

st.subheader("Project Features")

features = [
    "Website Crawling",
]

for feature in features:
    st.markdown(f"✅ {feature}")

st.divider()

st.info(
    "Run a website audit to start seeing analytics here."
)
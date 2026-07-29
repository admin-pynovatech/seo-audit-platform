import streamlit as st
import pandas as pd
from services.crawler import WebsiteCrawler

st.title("🌐 Website Crawler")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("Start Crawl"):

    if not url.strip():
        st.warning("Please enter a website URL.")
        st.stop()

    crawler = WebsiteCrawler()

    with st.spinner("Crawling website..."):

        result = crawler.crawl(url)

    if result["success"]:

        st.success(result["message"])

        # -----------------------------
        # Crawl Information
        # -----------------------------
        col1, col2, col3 = st.columns(3)

        def metric_card(title, value, icon):
            st.markdown(
                f"""
                <div style="
                    border:1px solid #ddd;
                    border-radius:10px;
                    padding:20px;
                    text-align:center;
                    box-shadow:2px 2px 8px rgba(0,0,0,0.08);
                ">
                    <h4>{icon} {title}</h4>
                    <h2>{value}</h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col1:
            metric_card("Status Code", result["status_code"], "📡")

        with col2:
            metric_card("Response Time", f"{result['response_time']:.2f} sec", "⏱️")

        with col3:
            metric_card("Redirects", result["redirects"], "🔄")

        st.write("**Final URL:**")
        st.code(result["url"])

        # -----------------------------
        # Page Information
        # -----------------------------
        st.divider()
        st.header("📄 Page Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Title**")
            st.write(result["title"])

            st.write("**Content Type**")
            st.write(result["content_type"])

            st.write("**Encoding**")
            st.write(result["encoding"])

        with col2:
            st.write("**Server**")
            st.write(result["server"])

            st.write("**Content Length**")
            st.write(result["content_length"])

            st.write("**Protocol**")
            st.write(result["protocol"])

        # -----------------------------
        # Page Statistics
        # -----------------------------
        st.divider()
        st.header("📊 Page Statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Links",
                result["links"]
            )

        with col2:
            st.metric(
                "Images",
                result["images"]
            )

        with col3:
            st.metric(
                "Scripts",
                result["scripts"]
            )

        # -----------------------------
        # HTTP Headers
        # -----------------------------

        st.divider()
        st.header("📡 HTTP Headers")

        for key, value in result["headers"].items():

            with st.expander(key):
                st.code(value)

    else:
        st.error(result["message"])
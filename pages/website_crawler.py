"""
Website Crawler page.
"""

import pandas as pd
import streamlit as st

from services.crawler import WebsiteCrawler

st.title("🌐 Website Crawler")

with st.form("crawl_form"):
    url = st.text_input(
        "Website URL",
        placeholder="https://example.com",
    )

    submitted = st.form_submit_button(
        "Start Crawl",
        type="primary",
    )

if submitted:

    if not url.strip():
        st.warning("Please enter a website URL.")
        st.stop()

    crawler = WebsiteCrawler()

    with st.spinner("Crawling website..."):
        result = crawler.crawl(url)

    if result["success"]:

        st.success(result["message"])

        # ==========================================
        # Crawl Information
        # ==========================================

        st.subheader("📡 Crawl Information")

        metrics = [
            ("Status Code", result["status_code"]),
            ("Response Time", f"{result['response_time']:.3f} sec"),
            ("Redirects", result["redirects"]),
        ]

        cols = st.columns(len(metrics))

        for col, (label, value) in zip(cols, metrics):
            with col:
                st.metric(label, value)

        st.write("**Final URL**")
        st.code(result["url"])

        # ==========================================
        # Page Information
        # ==========================================

        st.divider()
        st.subheader("📄 Page Information")

        page_info = pd.DataFrame(
            {
                "Property": [
                    "Title",
                    "Protocol",
                    "Content Type",
                    "Encoding",
                    "Server",
                    "Content Length",
                ],
                "Value": [
                    result["title"],
                    result["protocol"],
                    result["content_type"],
                    result["encoding"],
                    result["server"],
                    result["content_length"],
                ],
            }
        )

        st.dataframe(
            page_info,
            hide_index=True,
            width="stretch",
        )

        # ==========================================
        # Page Statistics
        # ==========================================

        st.divider()
        st.subheader("📊 Page Statistics")

        stats = [
            ("Links", result["links"]),
            ("Images", result["images"]),
            ("Scripts", result["scripts"]),
            ("Stylesheets", result.get("stylesheets", 0)),
        ]

        cols = st.columns(len(stats))

        for col, (label, value) in zip(cols, stats):
            with col:
                st.metric(label, value)

        # ==========================================
        # HTTP Response Headers
        # ==========================================

        st.divider()
        st.subheader("📑 HTTP Response Headers")

        headers_df = pd.DataFrame(
            result["headers"].items(),
            columns=["Header", "Value"],
        )

        st.dataframe(
            headers_df,
            hide_index=True,
            width="stretch",
        )

    else:
        st.error(result["message"])
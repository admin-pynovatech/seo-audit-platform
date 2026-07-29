"""
Website Crawler page.
"""

import pandas as pd
import streamlit as st

from services.crawler import WebsiteCrawler


st.title("🌐 Website Crawler")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com",
)

if st.button("Start Crawl", type="primary"):

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

        columns = st.columns(len(metrics))

        for column, (label, value) in zip(columns, metrics):
            with column:
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
            use_container_width=True,
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
            ("Stylesheets", result["stylesheets"]),
        ]

        columns = st.columns(len(stats))

        for column, (label, value) in zip(columns, stats):
            with column:
                st.metric(label, value)

        # ==========================================
        # HTTP Headers
        # ==========================================

        st.divider()
        st.subheader("📑 HTTP Response Headers")

        headers_df = pd.DataFrame(
            list(result["headers"].items()),
            columns=["Header", "Value"],
        )

        st.dataframe(
            headers_df,
            hide_index=True,
            use_container_width=True,
        )

    else:
        st.error(result["message"])
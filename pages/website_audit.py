import streamlit as st

from services.crawler import WebsiteCrawler

st.title("🌐 Website Audit")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("Start Audit"):

    crawler = WebsiteCrawler()

    result = crawler.crawl(url)

    if result["success"]:

        st.success(result["message"])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Status Code",
                result["status_code"]
            )

        with col2:
            st.metric(
                "Response Time",
                f'{result["response_time"]} sec'
            )

        with col3:
            st.metric(
                "Final URL",
                result["url"]
            )

    else:

        st.error(result["message"])
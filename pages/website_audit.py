import streamlit as st

from services.crawler import WebsiteCrawler

st.title("🌐 Website Audit")

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

if st.button("Start Audit"):

    if not url.strip():
        st.warning("Please enter a website URL.")
        st.stop()

    crawler = WebsiteCrawler()

    with st.spinner("Analyzing website..."):
        result = crawler.crawl(url)

    if result.get("success"):

        # st.write(result)      # chek the output testing

        st.success(result["message"])

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Status Code", result.get("status_code"))

        with col2:
            st.metric("Response Time", f"{result.get('response_time')} sec")

        with col3:
            st.metric("Final URL", result.get("url"))

        st.divider()

        st.subheader("📄 Page Title")
        st.write(result.get("title", "Not Available"))

        st.subheader("📝 Meta Description")
        st.write(result.get("meta_description", "Not Available"))

        st.subheader("🏷️ Headings")
        st.json(result.get("headings", {}))

    else:
        st.error(result.get("message", "Unknown error"))
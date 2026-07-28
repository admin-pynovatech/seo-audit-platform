import streamlit as st

from services.crawler import WebsiteCrawler
from utils.helpers import show_audit_card
from utils.score import SEOScoreCalculator

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
        calculator = SEOScoreCalculator(result)
        dashboard = calculator.calculate()

    if result["success"]:

        # Create dashboard data
        calculator = SEOScoreCalculator(result)
        dashboard = calculator.calculate()

        st.success(result["message"])

        # -----------------------------
        # SEO Dashboard
        # -----------------------------
        st.header("📊 SEO Dashboard")

        st.metric(
            "SEO Score",
            f'{dashboard["seo_score"]}/100'
        )

        st.progress(
            dashboard["seo_score"] / 100
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(f'Pass\n\n{dashboard["summary"]["Pass"]}')

        with col2:
            st.warning(f'Warning\n\n{dashboard["summary"]["Warning"]}')

        with col3:
            st.error(f'Fail\n\n{dashboard["summary"]["Fail"]}')

        # -----------------------------
        # Website Information
        # -----------------------------
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Status Code", result["status_code"])

        with col2:
            st.metric("Response Time", f'{result["response_time"]} sec')

        with col3:
            st.metric("Final URL", result["url"])

        # -----------------------------
        # SEO Data
        # -----------------------------
        st.divider()

        st.subheader("📄 Page Title")
        st.write(result["title"])

        st.subheader("📝 Meta Description")
        st.write(result["meta_description"])

        st.subheader("🏷️ Headings")
        for tag, items in result["headings"].items():
            st.markdown(f"### {tag} ({len(items)})")
            if items:
                for item in items:
                    st.write(f"• {item}")
            else:
                st.caption("None")

        # -----------------------------
        # SEO Audit
        # -----------------------------
        st.divider()

        st.header("📈 SEO Audit")

        show_audit_card(
            "Title Tag",
            result["title_analysis"]
        )

        show_audit_card(
            "Meta Description",
            result["meta_analysis"]
        )

        show_audit_card(
            "H1 Tag",
            result["h1_analysis"]
        )

    else:
        st.error(result["message"])
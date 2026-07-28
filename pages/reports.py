import os
from pathlib import Path

import streamlit as st

st.title("📄 Reports")

REPORTS_DIR = Path("reports")

if not REPORTS_DIR.exists():
    st.warning("Reports folder not found.")
    st.stop()

files = []

for root, _, filenames in os.walk(REPORTS_DIR):
    for filename in filenames:
        files.append(Path(root) / filename)

if not files:
    st.info("No reports available.")
    st.stop()

st.success(f"Found {len(files)} report(s).")

for file in sorted(files, reverse=True):

    st.divider()

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"**{file.name}**")
        st.caption(file.parent.name.upper())
        st.caption(f"{round(file.stat().st_size / 1024, 2)} KB")

    with col2:
        with open(file, "rb") as f:
            st.download_button(
                "Download",
                data=f,
                file_name=file.name,
                mime="application/octet-stream",
                key=file.name
            )
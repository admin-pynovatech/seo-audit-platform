"""
Helper functions for reusable Streamlit UI components.
"""

import streamlit as st


def show_info_card(title: str, data: dict) -> None:
    """
    Display a reusable information card.

    Args:
        title: Card title.
        data: Dictionary containing key-value pairs to display.
    """
    with st.container(border=True):
        st.subheader(title)

        for key, value in data.items():
            label = key.replace("_", " ").title()
            st.write(f"**{label}:** {value}")
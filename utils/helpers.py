import streamlit as st


def show_audit_card(title: str, data: dict):

    status = data["status"]

    if status == "Pass":
        st.success(f"✅ {title}")
    elif status == "Warning":
        st.warning(f"⚠️ {title}")
    else:
        st.error(f"❌ {title}")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Score", f'{data["score"]}/10')

    with col2:
        st.metric("Status", data["status"])

    # Display additional fields if available
    for field in ["length", "count", "coverage", "found", "total"]:

        if field in data:
            st.write(
                f"**{field.replace('_', ' ').title()}:** {data[field]}"
            )

    # Display value
    if "value" in data:

        if isinstance(data["value"], dict):

            st.write("**Properties:**")

            for key, value in data["value"].items():
                st.write(f"**{key}:** {value}")

        else:

            st.write("**Value:**")
            st.write(data["value"])

    st.info(data["message"])
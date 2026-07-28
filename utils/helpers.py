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
        st.metric("Status", status)

    if "length" in data:
        st.write(f"**Length:** {data['length']}")

    if "count" in data:
        st.write(f"**Count:** {data['count']}")

    if "value" in data:
        st.write(f"**Value:**")
        st.write(data["value"])

    st.info(data["message"])
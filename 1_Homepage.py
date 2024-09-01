import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🧊",
)

st.title("Homepage")
st.sidebar.success("Welcome to the homepage!")

st.divider()

st.header("Let's get started!")

st.write(
    """
    Welcome to the homepage of FitBit code execution project! 🚀

    Select the page you want to navigate to from the sidebar.

    """
)

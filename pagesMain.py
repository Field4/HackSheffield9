import streamlit as st

# Set up the home page
st.set_page_config(
    page_title="Streamlit Multi-Page App",
    page_icon=":sparkles:",
    layout="wide",
)

# Add logo and title
st.sidebar.image("logo.png")
st.sidebar.title("Navigation")
st.sidebar.markdown("Select a page from the sidebar.")

# Home Page Content
st.title("Welcome to the Streamlit App")
# st.image("header_image.jpg", caption="Aesthetically Pleasing App")

st.markdown(
    """
    This app demonstrates a multi-page structure in Streamlit with the following sections:
    - **Graphs**: Displays graphs in two columns.
    - **Animation**: Showcases animations.
    - **Settings**: Customize the app.
    """
)
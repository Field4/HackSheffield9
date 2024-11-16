import streamlit as st 

st.set_page_config(
    page_title="Graphs",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Graphs")
st.markdown("These are our graphs for displaying animal populations and food avilability.")
col1, col2 = st.columns(2)
with col1:
    st.title("Some Graphs")

with col2: 
    st.title("Other Graphs")



import streamlit as st 
def showPage():
    st.title("Graph")
    st.subheader("These are our graphs for displaying animal populations and food avilability")
    col1, col2 = st.columns(2)
    with col1:
        st.title("Some Graphs")

    with col2: 
        st.title("Other Graphs")



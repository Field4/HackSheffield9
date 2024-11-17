import streamlit as st 
#import connectionTest
import main

st.set_page_config(
    page_title="Graphs",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Graphs")
st.markdown("These are our graphs for displaying animal populations and food avilability.")
col1, col2 = st.columns(2)
# df1, df2, df3 = connectionTest.create_graphs()
df1 = main.main()
df3 = main.main()
#with col1:
st.title("Some Graphs")
st.line_chart(df1)
    #st.line_chart(df2)

#with col2: 
    #st.title("Other Graphs")
    #st.line_chart(df3)



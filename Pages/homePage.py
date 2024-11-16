import streamlit as st 


st.set_page_config(
    page_title="Home",
    page_icon=":house:",
    layout="wide",
)

st.title("Home")
st.markdown("This project is a simulation of the growth and decline in a population. It represents three elements of an ecosystem: The producers, the herbivores and the carnivores.")
st.markdown("We have produced two ways of viewing the results:")
st.markdown(" - The first way is using graphs - We have one graph per population so you can see how they grow and decline over time")
st.markdown(" - The second way is through an animation on a map, (explain map here)")


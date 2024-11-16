import streamlit as st
import numpy as np
import pandas as pd

def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def about_page():
    st.title("About Page")
    st.write("This is the About Page!")

def contact_page():
    st.title("Contact Page")
    st.write("Reach out to us on the Contact Page!")

# Sidebar navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    options=["Home", "About", "Contact"]
)

# Render the selected page
if menu == "Home":
    home_page()
elif menu == "About":
    about_page()
elif menu == "Contact":
    contact_page()
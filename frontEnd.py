import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

import graphPage
import homePage
import settingsPage
import animationPage

selected = "Home"
with st.sidebar:
    selected = option_menu("Main Menu", ["Home","Graph", "Animation","Settings"],
    icons = ['house', 'graph-up', 'tv','gear'], menu_icon = "cast", default_index=1)


if selected == "Home":
    homePage.showPage()
elif selected == "Graph":
    graphPage.showPage() 
elif selected == "Settings":
    settingsPage.showPage()
else:
    animationPage.showPage()

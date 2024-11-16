import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

import graphPage
import homePage
import settingsPage
import animationPage



l1 = "Home"
l2 = "Graph"
l3 = "Animation"
l4 = "Settings"
l5 = "Adjust font size"
l6 = "Text size : "


# def change_label_style(label, font_size=12, font_color='black', font_family='sans-serif'):
#    font_size = str(font_size) + "px"
#    html = f"""
#    <script>
#        var elems = window.parent.document.querySelectorAll('p');
#        var elem = Array.from(elems).find(x => x.innerText == '{label}');
#        elem.style.fontSize = '{font_size}';
#        elem.style.color = '{font_color}';
#        elem.style.fontFamily = '{font_family}';
#    </script>
#    """
#    st.components.v1.html(html) 

# with st.popover("Adjust Font Size"):
 #   textSize = st.text_input("Input Font Size: ")

# st.write(change_label_style(l6,textSize), textSize)
selected = "Home"
with st.sidebar:
    selected = option_menu("Main Menu", [l2,l1, l3,l4],
    icons = ['graph-up', 'house', 'tv','gear'], menu_icon = "menu-app", default_index=1)


if selected == "Home":
    homePage.showPage()
elif selected == "Graph":
    graphPage.showPage() 
elif selected == "Settings":
    settingsPage.showPage()
else:
    animationPage.showPage()

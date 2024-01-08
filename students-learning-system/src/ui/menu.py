from streamlit_option_menu import option_menu
import sys
sys.path.append('../')
import streamlit as st
from ui.page import Page

class Menu(Page):
    """
    The Page is the Menu page, which always shows and has links between the pages.

    ...

    Methods
    -------
    display()
        Displays the menu onto the screen for the student to see.
    """

    def display(self):
        """Displays the menu onto the screen for the student to see."""
        if 'choose' not in st.session_state:
            st.session_state['choose'] = None
        with st.sidebar:
            st.session_state['choose'] = option_menu("Student Event Tracker", ["Dashboard", "IDE", "pptx", "Dataset"],
                                    icons=['house', 'book', 'camera fill', 'kanban'],
                                    menu_icon="app-indicator", default_index=0,
                                    styles={
                    "container": {"padding": "5!important", "background-color": "#fafafa"},
                    "icon": {"color": "purple", "font-size": "25px"},
                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                    "nav-link-selected": {"background-color": "#05ab21"}, ##02ab21
                }
            )

        


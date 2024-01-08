import streamlit as st
import sys
sys.path.append('../')
from ui.page import Page

class StudentInfo(Page):
    """
    The Page is the student information page, which shows all the relevant details for the student.

    ...

    Attributes
    ----------
    data : pandas.Dataframe
        A dataframe representing the given student information.

    Methods
    -------
    display()
        Displays the student info webpage onto the screen for the student to see.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : pandas.Dataframe
            A dataframe representing the given student information.
        """
        self.data = data

    def display(self):
        """Displays the student info webpage onto the screen for the student to see."""
        st.table(self.data)

import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
import time
from ui.page import Page


class Dashboard(Page):
    """
    The Page is the dashboard page, which shows a summary of all the materials for the student.

    ...

    Attributes
    ----------
    DashB: pandas.Dataframe
        This is the dashboard information for the student.

    Methods
    -------
    display()
        Displays the dashboard webpage onto the screen for the student to see.

    """

    def __init__(self, dashboard_data):
        """
        Parameters
        ----------
        dashboard_data : dict
            This is the dashboard information for the student.
        """
        self.DashB = dashboard_data.loc[:, ~dashboard_data.columns.str.contains('^Unnamed')]



    def display(self):
        """Displays the dashboard webpage onto the screen for the student to see."""


        '''
        
Title: Beyond Code

Objective: Navigating Career Opportunities in Ever-Evolving Software Industry through Real-world Industry Scenarios.

Speakers: 
1. Keerthivasan Santhanakrishnan - https://www.linkedin.com/in/keerthivasan-santhanakrishnan-314029a1/
2. Karthik Ravichandran - https://www.linkedin.com/in/karthik-ravichandran-181173a9/
3. Anto Peter Felix Amalraj - https://www.linkedin.com/in/anto-peter/
4. Rubesh Sivasamy - https://www.linkedin.com/in/rubesh-sivasamy/

Below are the timings,
JAN 12 2024 8 AM EST
JAN 19 2024 8 AM EST
JAN 26 2024 8 AM EST
FEB 2 2024 8 AM EST
FEB 9 2024 8 AM EST
FEB 16 2024 8 AM EST
FEB 23 2024 8 AM EST
MAR 1 2024 8 AM EST
MAR 8 2024 8 AM EST
MAR 15 2024 8 AM EST
MAR 22 2024 8 AM EST
MAR 29 2024 8 AM EST

        '''

        st.header("Beyond Code")
        st.subheader('Objective :chart_with_upwards_trend:')

        st.caption("Navigating Career Opportunities in Ever-Evolving Software Industry through Real-world Industry Scenarios.")

        st.subheader('Session info')
        st.dataframe(self.DashB)

        st.subheader('Speakers')
        # Create four columns
        col1, col2, col3, col4 = st.columns([1,1,1,1])

        # Display images in separate columns
        col1.image('../data/speakers/Anto.jpeg', caption='Anto Peter Felix Amalraj - https://www.linkedin.com/in/anto-peter/', use_column_width=True)
        col2.image('../data/speakers/Karthik.jpg', caption='Karthik Ravichandran - https://www.linkedin.com/in/karthik-ravichandran-181173a9/', use_column_width=True)
        col3.image('../data/speakers/keerthi.jpeg', caption='Keerthivasan Santhanakrishnan - https://www.linkedin.com/in/keerthivasan-santhanakrishnan-314029a1/', use_column_width=True)
        col4.image('../data/speakers/Rubesh.jpeg', caption='Rubesh Sivasamy - https://www.linkedin.com/in/rubesh-sivasamy/', use_column_width=True)

        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
from ui.page import Page

class Gradescope(Page):
    """
    The Page is the gradescope page, which shows all the relevant gradescope info for each course.

    ...

    Attributes
    ----------
    courses : List
        A list of courses which the student is enrolled in for display
    data : dict
        A dict representing a mapping from course name to course information from gradescope for each class.

    Methods
    -------
    display()
        Displays the gradescope webpage onto the screen for the student to see.
    display_course(data)
        Displays the given course information onto the screen.
    """

    def __init__(self, courses, data):
        """
        Parameters
        ----------
        courses : List
            A list of courses which the student is enrolled in for display
        data : dict
            A dict representing a mapping from course name to course information from gradescope for each class.
        """
        self.courses = courses
        self.data = data

    def display(self):
        """Displays the gradescope webpage onto the screen for the student to see."""
        for course in self.courses:
            st.subheader(f'_Class {course} Gradescope_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
            if self.data[course] is None:
                st.caption('Check Moodle for this course')
            else:
                self.display_course(*self.data[course])

    def display_course(self, hws, stats, score):
        """
        Displays the given course information onto the screen.

        Parameters
        ----------
        hws : pandas.Dataframe
            The homework information for this course
        stats : pandas.Dataframe
            The statistics for each assignment for the whole class
        score : pandas.Dataframe
            The raw grades this student got on gradescope
        """
        st.caption('Homework Description and due date')
        st.dataframe(
                hws,
                column_config={
                    "Done": st.column_config.CheckboxColumn(
                        "Done",
                        help="Select your **favorite** widgets",
                        default=False,
                    ),
                    "Title": "Title",
                    "Description": "Description",
                    # "index": "HW",
                    "Due Date": st.column_config.DateColumn(),

                },
                hide_index=False,
                width=2000,
                height=180
            )
        # with c1:
        st.caption('Your Grade summary and class stats')
        st.dataframe(
            pd.concat([stats.T, score], axis=1),
            column_config = {"TODO": "Your Score"},
            hide_index=False,
            width=2000,
            height=180
        )

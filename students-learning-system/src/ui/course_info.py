import streamlit as st
import sys
sys.path.append('../')
from ui.page import Page

class CourseInfo(Page):
    """
    The Page is the course information page, which shows all the relevant details for each course.

    ...

    Attributes
    ----------
    courses : List
        A list of courses which the student is enrolled in for display
    data : dict
        A dict representing a mapping from course name to course information from moodle for each class.

    Methods
    -------
    display()
        Displays the Course info webpage onto the screen for the student to see.
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
            A dict representing a mapping from course name to course information from moodle for each class.
        """
        self.courses = courses
        self.data = data

    def display(self):
        """Displays the Course info webpage onto the screen for the student to see."""
        option = st.selectbox('Select the course to view the details',self.courses, disabled=False)
        st.subheader(f'_Class {option} Information_', divider='rainbow')
        self.display_course(self.data[option])

    def display_course(self, data):
        """
        Displays the given course information onto the screen.

        Parameters
        ----------
        data : pandas.Dataframe
            A dataframe which contains all the moodle information for the given course to display.
        """
        description = data[0]
        st.caption(description["Course Title"])
        st.caption("Syllabus")
        st.markdown(description["Course Syllabus"])
        st.caption("Grade Breakdown")
        st.table(description["Grade Breakdown"])

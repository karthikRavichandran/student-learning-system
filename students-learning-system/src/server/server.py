import pandas as pd
import streamlit as st
from database.dataloader import Dataloader
from database.firebase_data_download import DownloadDataFirebase
from ui.menu import Menu
from ui.gradescope import Gradescope
from ui.dashboard import Dashboard
from ui.piazza import Piazza
from ui.course_info import CourseInfo
from ui.student_info import StudentInfo
from ui.moodle import Moodle
from ui.ide import Ide
import os

class Server:
    """
    The server object is used to link the three components of the project together. 
    It generates and manages the UI objects as well as the switching of pages, 
    as well as retrieving the database materials.

    ...

    Attributes
    ----------
    student_id : int
        The student id for which data which is currently being accessed and served
    courses : list[str]
        the list of courses the student is enrolled in
    dataloader: Dataloader
        the dataloader object which will load all the relevant information for this student
    menu: Page
        the menu page which can be displayed (similar for dashboard, piazza, etc)
    Methods
    -------
    _dataload()
        Loads in the data from the local directory into the server
    _page_call()
        Initializes each of the pages for the given student and starts displaying them
    __download_data()
        Download data from the cloud to the local directory
    display_loop()
        Display the UI and await the users command to begin switching pages
    """
    
    def __init__(self, student_id):
        """
        Parameters
        ----------
        student_id : int
            The student id for which data which is currently being accessed and served
        """
        self.student_id = student_id
        self.all_courses = ["lang101", "math314", "phys999"]
        self.courses = [x for x in self.all_courses if str(self.student_id) in Dataloader.get_course_enrollment(f"../data/moodle/{x}.json")]
        self._dataload()
        self._page_call()

    def _dataload(self):
        """Loads in the data from the local directory into the server"""
        self.dataloader = Dataloader(self.student_id)
        self.menu = Menu()
        self.dashboard_data = self.dataloader.get_dashboard_data(f"../data/dashboard/dashboard.json")\
                             if os.path.exists(f"../data/dashboard/dashboard.json") else None

        self.piazza_data = {course : 
                            (self.dataloader.get_piazza_df(f"../data/piazza/{course}.json") 
                             if os.path.exists(f"../data/piazza/{course}.json") else None)
                            for course in self.courses}
        self.gradescope_data = {course : 
                            (self.dataloader.get_gradescope_data(f"../data/gradescope/{course}.json") 
                             if os.path.exists(f"../data/gradescope/{course}.json") else None)
                            for course in self.courses}
        self.moodle_data = {course : 
                            (self.dataloader.get_moodle_data(f"../data/moodle/{course}.json") 
                             if os.path.exists(f"../data/moodle/{course}.json") else None)
                            for course in self.courses}
        self.session_info = pd.read_csv('../data/session_vac.csv').reset_index(drop=True)
        
    def _page_call(self):
        """Initializes each of the pages for the given student and starts displaying them"""
        self.piazza = Piazza(self.courses, self.piazza_data)
        self.gradescope = Gradescope(self.courses, self.gradescope_data)
        self.dashboard = Dashboard(self.session_info)
        self.course_info = CourseInfo(self.courses, self.moodle_data)
        self.student_info = StudentInfo(self.dataloader.get_student_info())
        self.moodle = Moodle(self.courses, self.moodle_data)
        self.ide = Ide()
        self.menu.display()
        self.display_loop()


    def __download_data(self):
        """Download data from the cloud to the local directory"""
        download_data_firebase = DownloadDataFirebase()
        download_data_firebase.download_all_json()
        download_data_firebase.download_csv()

    def display_loop(self):
        """Display the UI and await the users command to begin switching pages"""
        if st.session_state['choose'] == "Dashboard":
            self.dashboard.display()
        elif st.session_state['choose'] == 'IDE':
            self.ide.display()
        elif st.session_state['choose'] == 'Piazza':
            self.piazza.display()
        elif st.session_state['choose'] == 'Course Info':
            self.course_info.display()
        elif st.session_state['choose'] == 'Student Info':
            self.student_info.display()
        elif st.session_state['choose'] == 'Moodle':
            self.moodle.display()

import streamlit as st
import sys
sys.path.append('../')
import pandas as pd
import time
from ui.page import Page
import subprocess
import os
import psutil


class Ide(Page):
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

    def __init__(self):
        """
        Parameters
        ----------
        dashboard_data : dict
            This is the dashboard information for the student.
        """
        self.port=8107


    def create_workspace(self, workspace_path):
        try:
            os.makedirs(workspace_path, exist_ok=True)
            st.success(f"Workspace created at {workspace_path}")
        except Exception as e:
            st.error(f"Error creating workspace: {e}")

    def launch_jupyter_lab(self, workspace_path, port):
        try:
            cmd = ['jupyter', 'lab', f'--port={port}', '--ip=127.0.0.1', f'--NotebookApp.notebook_dir={workspace_path}']
            self.process = subprocess.Popen(cmd, cwd=workspace_path)
            st.success(
                "Jupyter Lab is launching in the specified workspace. Please check your browser for the new tab.")
            return self.process.pid
        except subprocess.CalledProcessError as e:
            st.error(f"Error launching Jupyter Lab: {e}")
        finally:
            os.chdir(os.getcwd())  # Reset working directory to the original

    def kill_jupyter_lab(self):
        try:
            process = psutil.Process(st.session_state.jupyter_lab_pid)
            process.terminate()
            st.success(f"Jupyter Lab with PID {st.session_state.jupyter_lab_pid} terminated.")
        except Exception as e:
            st.error(f"Error terminating Jupyter Lab: {e}")

    def display(self):
        """Displays the dashboard webpage onto the screen for the student to see."""

        # Streamlit app
        st.title("Launch Jupyter Lab in Workspace from Streamlit")

        # Input box for workspace path
        workspace_path = st.text_input("Enter workspace path:", value="./my_workspace")

        # Input box for port number
        port = st.number_input("Enter Jupyter Lab port number", min_value=1, max_value=65535, step=1, value=self.port)

        # Button to create workspace and launch Jupyter Lab
        if st.button("Create Workspace and Launch Jupyter Lab"):
            self.create_workspace(workspace_path)
            st.session_state.jupyter_lab_pid = self.launch_jupyter_lab(workspace_path, port)
            st.success("Jupyter Lab is launching in the specified workspace. Please check your browser for the new tab.")

        if st.button("Kill Jupyter Lab"):
            if 'jupyter_lab_pid' in st.session_state:
                self.kill_jupyter_lab()
            else:
                st.warning("Jupyter Lab is not currently running.")


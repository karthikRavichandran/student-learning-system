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
        self.port=8100


    def create_workspace(self, workspace_path):
        try:
            os.makedirs(workspace_path, exist_ok=True)
            st.success(f"Workspace created at {workspace_path}")
        except Exception as e:
            st.error(f"Error creating workspace: {e}")

    def launch_jupyter_lab(self, workspace_path, port):
        st.session_state.port_in_use, st.session_state.existing_pid = self.is_port_in_use(port)
        if st.session_state.port_in_use:
            st.warning(f"Port {port} is already in use by process with PID {st.session_state.existing_pid}.")
            if st.button(f"Kill Jupyter Lab in port {port} with pid {st.session_state.existing_pid}"):
                self.kill_process(st.session_state.existing_pid)
                # You can add additional code here to launch your new process with the specified port
        else:
            st.success(f"Port {port} is available.")
            try:
                cmd = ['jupyter', 'lab', f'--port={port}', '--ip=127.0.0.1', f'--NotebookApp.notebook_dir={workspace_path}']
                self.process = subprocess.Popen(cmd, cwd=workspace_path)
                st.session_state.is_running = True
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
            st.success(f"Jupyter Lab with PID {st.session_state.jupyter_lab_pid} terminated and Port {self.port} is free.")
        except Exception as e:
            st.error(f"Error terminating Jupyter Lab: {e}")

    def is_port_in_use(self, port):
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['cmdline'] is not None and f'--port={port}' in proc.info['cmdline']:
                    return True, proc.info['pid']
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False, None

    def kill_process(self, pid):
        try:
            process = psutil.Process(pid)
            process.terminate()
            st.success(f"Process with PID {pid} terminated.")
        except Exception as e:
            st.error(f"Error terminating process: {e}")

    def display(self):
        """Displays the dashboard webpage onto the screen for the student to see."""

        # Streamlit app
        st.title("Launch Jupyter Lab in Workspace from Streamlit")

        # Input box for workspace path
        workspace_path = st.text_input("Enter workspace path:", value="./my_workspace")

        # Input box for port number
        # port = st.number_input("Enter Jupyter Lab port number", min_value=1, max_value=65535, step=1, value=self.port)
        port = self.port
        # Button to create workspace and launch Jupyter Lab
        if st.button("Create Workspace and Launch Jupyter Lab"):
            if 'is_running' in st.session_state:
                if not st.session_state.is_running:
                    with st.spinner("creating workspace and launching Lab..."):
                        # Simulate a long-running task
                        time.sleep(5)
                        self.create_workspace(workspace_path)
                        st.session_state.jupyter_lab_pid = self.launch_jupyter_lab(workspace_path, port)
                    #st.success("Jupyter Lab is launching in the specified workspace. Please check your browser for the new tab.")
                else:
                    st.warning("Another Jupyter Lab is currently running in port 8100.")
            else:
                st.session_state.is_running = False
        if 'jupyter_lab_pid' in st.session_state:
            # st.write(f"Jupyter Lab is running. You can't launch another: PID {st.session_state.jupyter_lab_pid}")
            if st.button("Kill Jupyter Lab"):
                if st.session_state.jupyter_lab_pid is not None:
                    with st.spinner("Killing the workspace..."):
                        # Simulate a long-running task
                        time.sleep(5)
                        self.kill_jupyter_lab()
                        st.session_state.is_running = False
                        st.session_state.jupyter_lab_pid = None


                else:
                    st.warning("Jupyter Lab is not currently running.")


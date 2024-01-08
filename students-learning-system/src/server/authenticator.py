import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from database.dataloader import Dataloader

class Authenticator:
    """
    The authenticator object which handles the authentication process before 
    allowing the user to access their information.

    ...

    Methods
    -------
    authenticate()
        This method begins the authentication process, verifying the 
        user's identity and returning their student id if their credentials are valid.
    """
    
    def authenticate(self):
        """
        This method begins the authentication process, verifying the 
        user's identity and returning their student id if their credentials are valid.
        """
        with open('../data/config.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)

        # credentials – The dictionary of usernames, names, passwords, and emails

        cookies = {"expiry_days":30, "key": "cook", "name": "cs520"}

        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )

        authenticator.login('Login', 'main')

        # Assigning  Calling Session state for authentication
        if st.session_state["authentication_status"]:
            authenticator.logout('Logout', 'main', key='unique_key')
            st.write(f'Welcome *{st.session_state["name"]}*')
            # if user give right Username and password, the line called menu()
            name = st.session_state["name"]
            student_info = Dataloader.get_all_student_info()
            return student_info[(student_info['first name'] == name.split()[0]) 
                                     & (student_info['last name'] == name.split()[1])]['student id']
        elif st.session_state["authentication_status"] is False:
            # Error Message is displayed in UI if User credentials didn't match.
            st.error('Username/password is incorrect')

        elif st.session_state["authentication_status"] is None:
            # This is when session_state of authentication_status is None i.e., when the app starts and
            # no one is logged in
            st.warning('Please enter your username and password')
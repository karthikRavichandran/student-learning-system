from server.server import Server
from server.authenticator import Authenticator
import streamlit as st

if __name__ == "__main__":
    auth = Authenticator()
    sid = auth.authenticate()
    if st.session_state["authentication_status"]:
        if 'sid' not in st.session_state:
            st.session_state['sid'] = sid.values[0]
        Server(sid.values[0])
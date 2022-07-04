import streamlit as st
from util import cookie_manager

def render():
    if st.button("Logout"):
        cookies = cookie_manager.get()
        cookies['token'] = ''
        cookies['user_email'] = ''
        
        st.experimental_rerun()

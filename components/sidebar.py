import streamlit as st
from auth import logout_button

def render():
    with st.sidebar:
        st.title('Welcome to my Streamlit App!')

        if st.button('Names'):
            st.session_state['page'] = 'names'

        if st.button('Faces'):
            st.session_state['page'] = 'faces'


        logout_button.render()
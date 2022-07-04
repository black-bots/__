import asyncio, streamlit as st
from auth import google_oauth

def render():
    authorization_url = asyncio.run(
        google_oauth.write_authorization_url()
    )

    st.write(f'''
        <h1>
            Please login using this 
            <a target="_self" href="{authorization_url}">url</a>
        </h1>''',
        unsafe_allow_html=True
    )
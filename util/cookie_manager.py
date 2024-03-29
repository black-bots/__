import streamlit as st
import os
from util.encrypted_cookie_manager import EncryptedCookieManager

# Retrieving client_secret environment variable with a default value of None
client_secret = os.environ.get('CLIENT_SECRET', None)

# Check if client_secret is None or not before proceeding
if client_secret is None:
    st.error("Client secret not found. Make sure you have set the CLIENT_SECRET environment variable.")
    st.stop()

# This should be on top of your script
cookies = EncryptedCookieManager(
    # This prefix will get added to all your cookie names.
    # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
    prefix="streamlit_proxy/",
    # You should really setup a long COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
    password=client_secret,
)

if not cookies.ready():
    # Wait for the component to load and send us current cookies.
    st.stop()

def get():
    return cookies

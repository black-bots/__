import streamlit as st, json, os, asyncio

from auth import google_oauth
from util import cookie_manager

def is_logged_in():
    cookies = cookie_manager.get()

    if not 'token' in cookies or cookies['token'] == '':
        try:
            code = st.experimental_get_query_params()['code']
        except:
            return False

        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    google_oauth.write_access_token(code)
                )

            except:
                return False

            else:
                if token.is_expired():
                    return False

                else:
                    cookies['token'] = json.dumps(token)

                    _, user_email = asyncio.run(
                        google_oauth.get_email(token['access_token'])
                    )

                    cookies['user_email'] = user_email

                    cookies.save()

                    return True

    else:
        token = google_oauth.json_str_to_token(cookies['token'])

        return not token.is_expired()

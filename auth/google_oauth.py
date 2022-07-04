import os, json
from typing import cast, Dict, Any
from httpx_oauth.clients.google import GoogleOAuth2
from httpx_oauth.oauth2 import OAuth2Token

client_id = os.environ['GOOGLE_CLIENT_ID']
client_secret = os.environ['GOOGLE_CLIENT_SECRET']
redirect_uri = os.environ['REDIRECT_URI']

client = GoogleOAuth2(client_id, client_secret)

def get_client():
    return client

async def write_authorization_url():
    client = get_client()

    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )

    return authorization_url


async def write_access_token(code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_email(token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


def json_str_to_token(token):
    return OAuth2Token(cast(Dict[str, Any], json.loads(token)))
# Streamlit Sample App w/ Discord OAuth
This is a sample Streamlit app, which should make for quick python development of web tools, similar to R Shiny apps. It's fairly straightforward and requires no web development or Javascript experience. See their full docs [here](https://docs.streamlit.io/). 

This Discord OAuth version is based on https://github.com/agreenspan24/sample-streamlit-with-google-oauth2 by Adam Greenspan.

## Development
To get started, clone the repo. Copy the `.env.sample` file and input the values from the Discord Authentication instructions below.
For development, I've used `pipenv` to standardize production.
1. Run `pipenv install` to download the relevant packages.
2. Run `pipenv shell` to create and enter a virtual environment .
3. Run `streamlit run app.py` to run the app locally. It can be refreshed from the page or automatically.

## Deployment
This project is dockerized, using the pipenv, so you can easily deploy it in the cloud or a virtual machine. If you want, add the environment variables into the docker compose file (securely).

## Discord Authentication
In addition, I've made this sample require Discord authentication.

To set up the discord authentication follow the following steps:
1.  Go to the [Discord Developers Portal](https://discord.com/developers/applications) page.
2.  Create **New Application** or select your existing one under **My Application**
3.  Fill in the necessary information.

Next, we need to setup OAuth2:

1.  Go to the  **OAuth2**
2.  Fill in redirect URIs for your application. These are the links you want the users to be redirected back to after logging in. For example, in local environment, you can use  `http://localhost:8501`
3.  Note down the  **Client ID**  and  **Client Secret**  for later.
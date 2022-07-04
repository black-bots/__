# Streamlit Sample App w/ Google OAuth
This is a sample Streamlit app, which should make for quick python development of web tools, similar to R Shiny apps. It's fairly straightforward and requires no web development or Javascript experience. See their full docs [here](https://docs.streamlit.io/). 

## Development
To get started, clone the repo. Copy the `.env.sample` file and input the values from the Google Authentication instructions below. 
For development, I've used `pipenv` to standardize production.
1. Run `pipenv install` to download the relevant packages.
2. Run `pipenv shell` to create and enter a virtual environment .
3. Run `streamlit run app.py` to run the app locally. It can be refreshed from the page or automatically.

## Deployment
This project is dockerized, using the pipenv, so you can easily deploy it in the cloud or a virtual machine. If you want, add the environment variables into the docker compose file (securely).

## Google Authentication
In addition, I've made this sample require Google authentication. You can control users with access in google cloud platform.

To set up the google authentication follow the following steps, borrowed from [this blog post](https://towardsdatascience.com/implementing-google-oauth-in-streamlit-bb7c3be0082c):
1.  Go to the Google API Console  [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)  page.
2.  Choose  **Internal**  so only users within your organization can access the app.
3.  Fill in the necessary information.
4.  Click Add Scopes and add any necessary scopes you require. For this example, we don’t need any.

Next, we need to create an authorization credential from GCP:

1.  Go to the  [Credentials page](http://credentials%20page/)  in GCP Console
2.  Click on  **Create Credentials > OAuth client ID.**
3.  Select  **Web Application** for  **Application type** and fill in the name for your client.
4.  Fill in redirect URIs for your application. These are the links you want the users to be redirected back to after logging in. For example, in local environment, you can use  `http://localhost:8501`
5.  Note down the  **Client ID**  and  **Client Secret**  for later.
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

credentials = None
__G_DRIVE_TOKEN_FILE = "token.pickle"
__OAUTH_SCOPE = ["https://www.googleapis.com/auth/drive"]
if os.path.exists(__G_DRIVE_TOKEN_FILE):
    with open(__G_DRIVE_TOKEN_FILE, 'rb') as f:
        credentials = pickle.load(f)
        if (
            (credentials is None or not credentials.valid)
            and credentials
            and credentials.expired
            and credentials.refresh_token
        ):
            credentials.refresh(Request())
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', __OAUTH_SCOPE)
    auth_url, _ = flow.authorization_url(prompt='consent')

    print(f"Please visit this URL to authorize this application: {auth_url}")

    code = input('Enter the authorization code: ')
    flow.fetch_token(code=code)
    credentials = flow.credentials

# Save the credentials for the next run
with open(__G_DRIVE_TOKEN_FILE, 'wb') as token:
    pickle.dump(credentials, token)

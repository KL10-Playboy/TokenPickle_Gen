import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the OAuth scopes required
SCOPES = ['https://www.googleapis.com/auth/drive']

# Path to the credentials file
CREDENTIALS_FILE = 'credentials.json'
# Path to the token file
TOKEN_FILE = 'token.pickle'

def main():
    creds = None

    # Check if the token file already exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
        # Refresh the token if it's expired
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        # If no valid credentials, initiate the OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        auth_url, _ = flow.authorization_url(prompt='consent')

        print('Please go to this URL and authorize the application:')
        print(auth_url)

        # After authorization, Google will redirect you to a URL with a code parameter
        auth_code = input('Enter the authorization code here: ')
        flow.fetch_token(code=auth_code)
        creds = flow.credentials

        # Save the credentials for future use
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    if creds and creds.valid:
        print('Authentication successful. Credentials have been saved to', TOKEN_FILE)
    else:
        print('Failed to obtain valid credentials.')

if __name__ == '__main__':
    main()

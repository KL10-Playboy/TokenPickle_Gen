import os
import pickle
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from utils import print_step, print_error, print_success, validate_credentials_file

# Define scopes with latest format - can be modified based on requirements
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/drive.readonly',
    'openid',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]

class TokenGenerator:
    def __init__(self):
        self.credentials = None
        self.token_file = 'token.pickle'
        self.credentials_file = 'credentials.json'

    def load_existing_token(self):
        """Attempt to load existing token if present"""
        try:
            if os.path.exists(self.token_file):
                with open(self.token_file, 'rb') as token:
                    self.credentials = pickle.load(token)
                return True
        except Exception as e:
            print_error(f"Error loading existing token: {str(e)}")
        return False

    def is_token_valid(self):
        """Check if current token is valid and refresh if needed"""
        if not self.credentials:
            return False

        if self.credentials.valid:
            return True

        if self.credentials.expired and self.credentials.refresh_token:
            try:
                self.credentials.refresh(Request())
                return True
            except Exception as e:
                print_error(f"Error refreshing token: {str(e)}")
                return False
        return False

    def save_token(self):
        """Save the token to pickle file with secure permissions"""
        try:
            with open(self.token_file, 'wb') as token:
                pickle.dump(self.credentials, token)
            # Set secure file permissions (read/write for owner only)
            os.chmod(self.token_file, 0o600)
            print_success(f"Token successfully saved to {self.token_file}")
            return True
        except Exception as e:
            print_error(f"Error saving token: {str(e)}")
            return False

    def generate_new_token(self):
        """Generate new OAuth2.0 token through web flow"""
        try:
            if not os.path.exists(self.credentials_file):
                print_error(f"Credentials file '{self.credentials_file}' not found!")
                print_step("\nTo comply with Google's new OAuth2.0 policy, please follow these steps:")
                print_step("1. Go to https://console.cloud.google.com")
                print_step("2. Create a new project or select existing one")
                print_step("3. Enable the required APIs (Gmail, Drive)")
                print_step("4. Configure OAuth consent screen:")
                print_step("   - Set User Type to 'External'")
                print_step("   - Fill required app information")
                print_step("   - Add test users if in testing mode")
                print_step("   - Add required scopes:")
                for scope in SCOPES:
                    print_step(f"     - {scope}")
                print_step("5. Create OAuth client ID:")
                print_step("   - Choose 'Desktop application' as application type")
                print_step("   - Set an appropriate name")
                print_step("6. Download and save the JSON file as 'credentials.json'")
                print_step("\nNote: Due to Google's security requirements:")
                print_step("- Your application may need verification if you plan to publish it")
                print_step("- Unverified apps can still be tested with test users")
                return False

            if not validate_credentials_file(self.credentials_file):
                return False

            flow = InstalledAppFlow.from_client_secrets_file(
                self.credentials_file, 
                SCOPES,
                redirect_uri='http://localhost:0'  # Use dynamic port
            )

            # Run local server for auth flow with updated parameters
            self.credentials = flow.run_local_server(
                port=0,  # Random port
                prompt='consent',  # Force consent prompt
                access_type='offline',  # Enable refresh token
                include_granted_scopes=True  # Include incremental authorization
            )

            return self.save_token()

        except Exception as e:
            print_error(f"Error generating new token: {str(e)}")
            return False

    def generate_token(self):
        """Main token generation process"""
        print_step("Starting OAuth2.0 token generation process...")

        # Try to load existing token
        if self.load_existing_token():
            print_step("Found existing token, checking validity...")
            if self.is_token_valid():
                print_success("Existing token is valid!")
                return True
            print_step("Existing token is invalid or expired")

        # Generate new token
        print_step("Generating new token...")
        if self.generate_new_token():
            print_success("Token generation completed successfully!")
            return True

        return False

def main():
    generator = TokenGenerator()
    if generator.generate_token():
        print_success("\nToken generation process completed successfully!")
        print_step(f"Token saved to: {generator.token_file}")
    else:
        print_error("\nToken generation failed. Please check the errors above and try again.")

if __name__ == "__main__":
    main()

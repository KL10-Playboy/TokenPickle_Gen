# OAuth 2.0 Token Generator

This project provides a Python script to generate and manage OAuth 2.0 tokens for accessing Google APIs such as Gmail and Google Drive. The script handles token creation, validation, and refreshing, ensuring secure and seamless authentication.

## Features

- **Token Management**: Automatically loads existing tokens, checks their validity, and refreshes them when necessary.
- **Secure Storage**: Tokens are saved securely with appropriate file permissions.
- **Guided Setup**: Provides step-by-step instructions to configure OAuth 2.0 credentials in the Google Cloud Console.
- **Comprehensive Validation**: Ensures the credentials file is correctly structured and contains all required fields.

## Prerequisites

- Python 3.6 or higher
- `google-auth`, `google-auth-oauthlib`, and `google-auth-httplib2` libraries

Install the required libraries using pip:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2
```

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/oauth-token-generator.git
   cd oauth-token-generator
   ```

2. **Configure OAuth 2.0 Credentials**:

   - Navigate to the [Google Cloud Console](https://console.cloud.google.com).
   - Create a new project or select an existing one.
   - Enable the required APIs (e.g., Gmail API, Google Drive API).
   - Configure the OAuth consent screen:
     - Set User Type to 'External'.
     - Fill in the required app information.
     - Add test users if in testing mode.
     - Add the necessary scopes:
       - `https://www.googleapis.com/auth/gmail.readonly`
       - `https://www.googleapis.com/auth/drive.readonly`
       - `openid`
       - `https://www.googleapis.com/auth/userinfo.email`
       - `https://www.googleapis.com/auth/userinfo.profile`
   - Create OAuth client ID:
     - Choose 'Desktop application' as the application type.
     - Set an appropriate name.
   - Download the JSON file and save it as `credentials.json` in the project directory.

3. **Run the Token Generator**:

   Execute the script to generate or refresh the token:

   ```bash
   python GenerateTokenPickle.py
   ```

   Follow the on-screen instructions to authenticate and authorize access. Upon successful completion, a `token.pickle` file will be created in the project directory.

## Security Considerations

- Ensure that both `credentials.json` and `token.pickle` files have secure permissions (read/write for the owner only). The script attempts to set these permissions automatically on Unix-based systems.
- Regularly review and rotate your credentials to maintain security.
- Be aware of Google's OAuth 2.0 policies, especially if you plan to publish the application. Unverified apps can still be tested with test users.

## Troubleshooting

- **Invalid Credentials File**: Ensure that `credentials.json` is correctly structured and contains all required fields. The script validates the file and provides specific error messages if issues are detected.
- **Token Generation Failure**: If the token generation fails, the script will display error messages to help identify the problem. Common issues include incorrect credentials or network problems.

For further assistance, refer to the [Google Identity Platform Documentation](https://developers.google.com/identity/protocols/oauth2) or open an issue in this repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This project is intended for educational and testing purposes. Ensure compliance with Google's policies and guidelines when using OAuth 2.0 in production applications.* 

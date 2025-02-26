# OAuth 2.0 Token Generator

This project provides a Python script to generate and manage OAuth 2.0 tokens for accessing Google APIs such as Gmail and Google Drive. The script handles token creation, validation, and refreshing, ensuring secure and seamless authentication.

## Features

- **Token Management**: Automatically loads existing tokens, checks their validity, and refreshes them when necessary.
- **Secure Storage**: Tokens are saved securely with appropriate file permissions.
- **Guided Setup**: Provides step-by-step instructions to configure OAuth 2.0 credentials in the Google Cloud Console.
- **Comprehensive Validation**: Ensures the credentials file is correctly structured and contains all required fields.

# Overview
This script (`GenerateTokenPickle.py`) automates the OAuth 2.0 authentication process for accessing Google APIs, such as Gmail and Google Drive. It checks for an existing authentication token, validates it, refreshes it if necessary, or initiates a new authentication flow if no valid token is found. The authenticated token is securely stored as `token.pickle` for future use.

# Running the Script

## Prerequisites
Before running this script, ensure the following:
1. **Python 3.x** is installed.
2. Required Python packages are installed:
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-auth-requests
   ```
3. A **Google Cloud project** is set up with OAuth 2.0 credentials.
4. The **`credentials.json`** file is present in the script directory.

## Google Cloud Setup (OAuth 2.0 Credentials)
Follow these steps to obtain OAuth credentials:
1. Visit the **Google Cloud Console**: [https://console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project or select an existing one.
3. Enable the required APIs (e.g., Gmail API, Google Drive API).
4. Configure the OAuth consent screen:
   - Choose `External` for User Type.
   - Fill in required application details.
   - Add test users if needed.
   - Add the following scopes:
     ```
     https://www.googleapis.com/auth/gmail.readonly
     https://www.googleapis.com/auth/drive.readonly
     openid
     https://www.googleapis.com/auth/userinfo.email
     https://www.googleapis.com/auth/userinfo.profile
     ```
5. Create OAuth Client ID:
   - Select `Desktop Application` as the Application Type.
   - Download the generated credentials file as `credentials.json`.
   - Place `credentials.json` in the same directory as `GenerateTokenPickle.py`.

## Installation and Running the Script
Run the following commands to install dependencies, clone the repository, and execute the script:
```bash
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

sudo apt update && sudo apt upgrade -y && sudo apt install git python3 python3-pip -y && sudo apt upgrade python3 -y && python3 -m pip install --upgrade pip && pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

git clone https://github.com/KL10-Playboy/TokenPickle_Gen

cd TokenPickle_Gen

wget -O credentials.json "direct_link_of_credentials.json"

ls

python3 GenerateTokenPickle.py
```

## Troubleshooting
### **Error: `credentials.json` Not Found**
- Ensure `credentials.json` is in the correct directory.
- Follow the Google Cloud setup steps to obtain credentials.

### **Error: Token Expired and Refresh Fails**
- Delete `token.pickle` and re-run the script.
- Ensure the OAuth consent screen and API access are properly configured.


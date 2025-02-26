# How To Generate Token Pickle Easily After Google Auth2.0 New Policy Update

This project provides a Python script to generate and manage OAuth 2.0 tokens for accessing Google APIs such as Gmail and Google Drive. The script handles token creation, validation, and refreshing, ensuring secure and seamless authentication.

## Features

- **Token Management**: Automatically loads existing tokens, checks their validity, and refreshes them when necessary.
- **Secure Storage**: Tokens are saved securely with appropriate file permissions.
- **Guided Setup**: Provides step-by-step instructions to configure OAuth 2.0 credentials in the Google Cloud Console.
- **Comprehensive Validation**: Ensures the credentials file is correctly structured and contains all required fields.

# Google Cloud Setup (OAuth 2.0 Credentials)

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

# Installation and Setup

## 1. Install Required Dependencies

```bash
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
```

## 2. Install Python and Required Packages

```bash
sudo apt update && sudo apt upgrade -y && sudo apt install git python3 python3-pip -y && sudo apt upgrade python3 -y && python3 -m pip install --upgrade pip && pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib google-auth google-auth-requests
```

## 3. Clone the Repository

```bash
git clone https://github.com/KL10-Playboy/TokenPickle_Gen
```

## 4. Move into the Project Directory

```bash
cd TokenPickle_Gen
```

## 5. Download `credentials.json`

Make sure your `credentials.json` file is present in your system. If not, download it using the command below:

```bash
wget -O credentials.json "direct_link_of_credentials.json"
```

## 6. Verify the File Presence

```bash
ls
```

## 7. Run the Script

```bash
python3 GenerateTokenPickle.py
```

## 8. Authenticate with Google

- Once you run the script, a URL will be generated.
- Copy and paste the URL into your browser.
- Log in with your Google account and allow permissions.
- After successful authentication, you will see the message: `The authentication flow has completed. You may close this window.`

## 9. Save the Generated Token

```bash
cp -r token.pickle /sdcard
```

## 10. Done! 🎉

You can now find `token.pickle` in your system. This token will be used for future authentication without needing to log in again.

# Troubleshooting

### **Error: `credentials.json` Not Found**
- Ensure `credentials.json` is in the correct directory.
- Follow the Google Cloud setup steps to obtain credentials.

### **Error: Token Expired and Refresh Fails**
- Delete `token.pickle` and re-run the script.
- Ensure the OAuth consent screen and API access are properly configured.

# Enjoy & Don't Forget to Star This Repo ⭐

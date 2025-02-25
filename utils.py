import json
import os
from typing import Any, Dict

def print_step(message: str) -> None:
    """Print a step message in blue"""
    print(f"\033[94m[*] {message}\033[0m")

def print_error(message: str) -> None:
    """Print an error message in red"""
    print(f"\033[91m[!] {message}\033[0m")

def print_success(message: str) -> None:
    """Print a success message in green"""
    print(f"\033[92m[+] {message}\033[0m")

def validate_credentials_content(creds_data: Dict[str, Any]) -> bool:
    """Validate the content of credentials data"""
    if 'installed' not in creds_data and 'web' not in creds_data:
        print_error("Invalid credentials file: missing 'installed' or 'web' key")
        return False

    # Get the correct credentials section
    creds_section = creds_data.get('installed') or creds_data.get('web')
    if not creds_section:
        print_error("Invalid credentials file structure")
        return False

    required_keys = [
        'client_id',
        'client_secret',
        'auth_uri',
        'token_uri',
        'redirect_uris'
    ]

    for key in required_keys:
        if key not in creds_section:
            print_error(f"Invalid credentials file: missing '{key}'")
            return False

    # Validate URLs for security
    if not creds_section['auth_uri'].startswith('https://'):
        print_error("Invalid auth_uri: must use HTTPS")
        return False

    if not creds_section['token_uri'].startswith('https://'):
        print_error("Invalid token_uri: must use HTTPS")
        return False

    # Validate redirect URIs
    valid_redirect_patterns = ['http://localhost', 'https://localhost']
    if not any(uri.startswith(tuple(valid_redirect_patterns)) 
               for uri in creds_section['redirect_uris']):
        print_error("Invalid redirect_uris: must include localhost URI")
        return False

    return True

def validate_credentials_file(credentials_file: str) -> bool:
    """
    Validate the structure and content of the credentials file
    """
    try:
        if not os.path.exists(credentials_file):
            print_error(f"Credentials file not found: {credentials_file}")
            return False

        # Check file permissions (should be readable only by owner)
        if os.name != 'nt':  # Skip on Windows
            file_mode = os.stat(credentials_file).st_mode & 0o777
            if file_mode != 0o600:
                print_step("Setting secure file permissions for credentials file")
                os.chmod(credentials_file, 0o600)

        with open(credentials_file, 'r') as f:
            creds_data = json.load(f)

        return validate_credentials_content(creds_data)

    except json.JSONDecodeError:
        print_error("Invalid credentials file: not valid JSON")
        return False
    except Exception as e:
        print_error(f"Error validating credentials file: {str(e)}")
        return False

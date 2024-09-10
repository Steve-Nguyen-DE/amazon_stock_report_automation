
import requests
from .creds import amz_credentials
def get_access_token():
    token_response = requests.post(
        "https://api.amazon.com/auth/o2/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": amz_credentials["refresh_token"],
            "client_id": amz_credentials["lwa_app_id"],
            "client_secret": amz_credentials["lwa_client_secret"],
        },
    )
    access_token = token_response.json()["access_token"]
    return access_token
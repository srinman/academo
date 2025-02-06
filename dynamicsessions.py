import requests
import os
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
token = credential.get_token("https://dynamicsessions.io/.default")
access_token = token.token
# print(access_token)
# use the following command to get authtoken
# az account get-access-token --resource https://dynamicsessions.io
# Configuration
endpoint = "https://westus2.dynamicsessions.io/subscriptions/3eef5dad-ad68-4246-8e02-e13d661de047/resourceGroups/academorg/sessionPools/my-session-pool/code/execute?api-version=2024-02-02-preview&identifier=my-session-pool"

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

# Payload
payload = {
    "properties": {
        "codeInputType": "inline",
        "executionType": "synchronous",
        "code": "print('Hello, world!')"
    }
}

# Send POST request
response = requests.post(endpoint, headers=headers, json=payload)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
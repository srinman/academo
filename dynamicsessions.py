import requests
import os
   
# use the following command to get authtoken
# az account get-access-token --resource https://dynamicsessions.io
# Configuration
endpoint = "https://westus2.dynamicsessions.io/subscriptions/3eef5dad-ad68-4246-8e02-e13d661de047/resourceGroups/academorg/sessionPools/my-session-pool/code/execute?api-version=2024-02-02-preview&identifier=my-session-pool"
authorization_token = os.getenv('AUTHORIZATION_TOKEN')

if not authorization_token:
    raise ValueError("Authorization token not found in environment variables")

# Headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {authorization_token}"
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
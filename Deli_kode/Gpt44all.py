# API konekcija za lokalini LLM GPT4All

import requests
import json

# URL of the local GPT-4All API server
api_url = "http://localhost:4891/v1/chat/completions"  # Adjust if your server is running on a different port or endpoint

# Define the headers (if needed, such as for content-type)
headers = {
    "Content-Type": "application/json"
}

# Define the payload (data to send)
data = {
    "model": "/sambanovasystems_-_SambaLingo-Slovenian-Chat",  # Replace with the model you're using locally
    "messages": [
        {"role": "user", "content": "Jaz sem matej pati"}
    ],
    "max_tokens": 150,  # Set the max number of tokens for the response
    "temperature": 0.7  # Adjust the temperature (creativity/randomness)
}

# Make the POST request to the local GPT-4All API server
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # Print the generated response
    print("Response:", response_data["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}, {response.text}")
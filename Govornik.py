import requests

# Define the URL and parameters
url = "https://s1.govornik.eu"
params = {
    "voice": "nik-unit",
    "text": "Pozdravljen na ta prekrasen dan.",
    "source": "PresernAI",
    "version": "1"
}

# Send the POST request
response = requests.post(url, data=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the MP3 file
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("MP3 file has been saved as 'output.mp3'")
else:
    print(f"Failed to fetch MP3. Status code: {response.status_code}, Response: {response.text}")

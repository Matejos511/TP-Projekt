import httpx
import asyncio

# Initialize PlayHT credentials
PLAYHT_USER_ID = "<F3YQlpnCXGT496lGRoMO0aztjaB3>"  # Replace with your actual PlayHT user ID
PLAYHT_API_KEY = "<4ed05e126d68468db84e39db7bb7ae6c>"  # Replace with your actual PlayHT API key
HEADERS = {
    "Authorization": f"Bearer {PLAYHT_API_KEY}",
    "X-User-ID": PLAYHT_USER_ID,
}

async def stream_audio(text, output_file="output.mp3"):
    url = "https://api.playht.com/v1/audio/stream"
    params = {
        "text": text,
        "voiceEngine": "Play3.0-mini",
    }

    async with httpx.AsyncClient() as client:
        try:
            # Start streaming the audio
            async with client.stream("POST", url, headers=HEADERS, json=params) as response:
                if response.status_code != 200:
                    print("Failed to start audio stream:", response.text)
                    return
                
                # Create or clear the output file
                with open(output_file, "wb") as file:
                    async for chunk in response.aiter_bytes():
                        file.write(chunk)

                print(f"Audio streaming complete. File saved as {output_file}")
        except Exception as e:
            print("Error during streaming:", e)

# Example usage
if __name__ == "__main__":
    asyncio.run(stream_audio("Yooohoooo, big summer blowout!"))

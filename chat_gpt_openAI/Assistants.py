
# client = Client(api_key="CLIENT_ID") 



import tkinter as tk
from tkinter import scrolledtext
import openai
import requests
import os
from playsound import playsound
import threading

# OpenAI API Key
openai.api_key = "APIKLJUC"

# Govornik API Configuration
govornik_url = "https://s1.govornik.eu"
govornik_voice = "nik-unit"
govornik_source = "PresernAI"
govornik_version = "1"

# MP3 file name for generated audio
mp3_file = "output.mp3"

# Function to handle sending user input to OpenAI API
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    chat_box.insert(tk.END, "You: " + user_input + "\n")

    # Call OpenAI API
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are France Prešeren."},
                {"role": "user", "content": user_input}
            ]
        )
        assistant_response = completion['choices'][0]['message']['content']
    except Exception as e:
        assistant_response = f"Error: {str(e)}"

    chat_box.insert(tk.END, "Assistant: " + assistant_response + "\n")

    # Call Govornik API to generate speech
    try:
        govornik_params = {
            "voice": govornik_voice,
            "text": assistant_response,
            "source": govornik_source,
            "version": govornik_version
        }
        response = requests.post(govornik_url, data=govornik_params)
        if response.status_code == 200:
            with open(mp3_file, "wb") as f:
                f.write(response.content)

            chat_box.insert(tk.END, "Assistant: Audio generated successfully. Click 'Play' to listen.\n")
        else:
            chat_box.insert(tk.END, f"Assistant: Failed to generate speech. Error {response.status_code}\n")
    except Exception as e:
        chat_box.insert(tk.END, f"Assistant: Error generating speech: {e}\n")

    input_box.delete("1.0", tk.END)

# Function to play the generated audio
def play_audio():
    if os.path.exists(mp3_file):
        threading.Thread(target=playsound, args=(mp3_file,)).start()
    else:
        chat_box.insert(tk.END, "Assistant: No audio file found. Please generate speech first.\n")

# Create the main application window
app = tk.Tk()
app.title("Chat with France Prešeren")

# Chat box to display conversation
chat_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=20, state="normal")
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Input box for user input
input_box = tk.Text(app, wrap=tk.WORD, width=50, height=5)
input_box.grid(row=1, column=0, padx=10, pady=10)

# "Send" button to send the message
send_button = tk.Button(app, text="Send", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# "Play" button to play the audio
play_button = tk.Button(app, text="Play", command=play_audio, width=10)
play_button.grid(row=1, column=2, padx=10, pady=10)

# Run the application
app.mainloop()

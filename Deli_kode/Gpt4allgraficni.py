import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import json

# GPT-4All local API endpoint
API_URL = "http://localhost:5000/v1/chat/completions"  # Update to your actual endpoint

# Function to send a message to the GPT-4All API
def send_message():
    user_input = user_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return

    # Display user's message in the chat log
    chat_log.insert(tk.END, f"You: {user_input}\n")
    user_entry.delete("1.0", tk.END)

    try:
        # Prepare API request
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "/sambanovasystems_-_SambaLingo-Slovenian-Chat",  # Replace with your model
            "messages": [{"role": "user", "content": user_input}],
            "max_tokens": 150,
            "temperature": 0.7,
        }

        # Send the request to the API
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the response
        response_data = response.json()
        bot_response = response_data["choices"][0]["message"]["content"]
    except Exception as e:
        bot_response = f"Error: {str(e)}"

    # Display GPT-4All's response in the chat log
    chat_log.insert(tk.END, f"GPT-4All: {bot_response}\n")
    chat_log.see(tk.END)

# Create the main application window
app = tk.Tk()
app.title("GPT-4All Chat")

# Chat log display
chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, state="normal", width=50, height=20)
chat_log.pack(padx=10, pady=10)

# User input field
user_entry = tk.Text(app, height=3, wrap=tk.WORD)
user_entry.pack(padx=10, pady=5)

# Send button
send_button = tk.Button(app, text="Send", command=send_message)
send_button.pack(pady=5)

# Start the Tkinter event loop
app.mainloop()

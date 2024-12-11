import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

# Replace with your GPT-4All API endpoint and API key
API_URL = "http://localhost:5000/api/v1/chat"
API_KEY = "your_api_key_here"  # If required

def send_message():
    user_input = user_entry.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a message!")
        return

    chat_log.insert(tk.END, f"You: {user_input}\n")
    user_entry.delete("1.0", tk.END)
    
    try:
        headers = {"Authorization": f"Bearer {API_KEY}"} if API_KEY else {}
        payload = {"prompt": user_input, "max_tokens": 150}
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        bot_response = response_data.get("response", "No response received.")
    except Exception as e:
        bot_response = f"Error: {str(e)}"

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

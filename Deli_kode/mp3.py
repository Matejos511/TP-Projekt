import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
import os

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

# Function to handle sending user input to the OpenAI API
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    # Display the user's input in the chat box
    chat_box.insert(tk.END, "Vi: " + user_input + "\n")
    
    # Call OpenAI API
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Vi ste France Prešeren."},
                {"role": "user", "content": user_input}
            ]
        )
        # Use `.content` to access the response text
        assistant_response = completion.choices[0].message.content
    except Exception as e:
        assistant_response = f"Napaka: {str(e)}"
    
    # Display the assistant's response in the chat box
    chat_box.insert(tk.END, "Prešeren: " + assistant_response + "\n")
    
    # Clear the input box
    input_box.delete("1.0", tk.END)

# Function to play the MP3 file
def play_mp3():
    mp3_file = "output.mp3"  # Replace with the path to your MP3 file
    os.startfile(mp3_file)

# Create the main application window
app = tk.Tk()
app.title("Pogovor z Francetom Prešerenom")

# Create a chat box to display the conversation
chat_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=20, state="normal")
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create an input box for the user to type their message
input_box = tk.Text(app, wrap=tk.WORD, width=50, height=5)
input_box.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(app, text="Pošlji", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Create a "Play" button to play the MP3 file
play_button = tk.Button(app, text="Play", command=play_mp3, width=10)
play_button.grid(row=2, column=0, padx=10, pady=10)

# Run the application
app.mainloop()

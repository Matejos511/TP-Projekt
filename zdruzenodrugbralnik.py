import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
import json
import os
import pygame

# GPT-4All lokalni API naslov
GPT4ALL_API_URL = "http://localhost:4891/v1/chat/completions"  # Prilagodite glede na vašo konfiguracijo

# Govornik API naslov
GOVORNIK_API_URL = "https://s1.govornik.eu"

# Inicializacija pygame za predvajanje zvoka
pygame.mixer.init()

# Funkcija za ustvarjanje govora iz besedila
def generate_speech(text, voice="nik2023"):
    params = {
        "voice": voice,
        "text": text,
        "source": "PresernAI",
        "version": "1"
    }

    try:
        response = requests.post(GOVORNIK_API_URL, data=params)
        if response.status_code == 200:
            # Shranimo MP3 datoteko
            output_file = "response.mp3"
            with open(output_file, "wb") as f:
                f.write(response.content)
            return output_file  # Vrne pot do shranjene datoteke
        else:
            print(f"Napaka pri ustvarjanju govora: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Napaka pri komunikaciji z govornikom: {str(e)}")
        return None

# Funkcija za predvajanje zvoka
def play_audio(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Počakamo, dokler se predvajanje ne konča
            pass
    except Exception as e:
        print(f"Napaka pri predvajanju zvoka: {str(e)}")

# Funkcija za pošiljanje sporočila in pridobitev odgovora
def send_message():
    user_input = user_entry.get("1.0", tk.END).strip()  # Preberemo uporabniško sporočilo
    if not user_input:
        messagebox.showwarning("Napaka vnosa", "Prosim, vnesite sporočilo!")
        return

    # Prikažemo uporabniško sporočilo v komunikatorju
    chat_log.insert(tk.END, f"Vi: {user_input}\n")
    user_entry.delete("1.0", tk.END)  # Pošiljanje izprazni vnosno polje

    try:
        # Priprava zahtevka za GPT-4All API
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "/sambanovasystems_-_SambaLingo-Slovenian-Chat",  # Zamenjajte z vašim modelom
            "messages": [{"role": "user", "content": user_input}],
            "max_tokens": 150,
            "temperature": 0.7,
        }

        # Pošljemo zahtevek na GPT-4All API
        response = requests.post(GPT4ALL_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Vrže izjemo, če pride do napake

        # Obdelava odgovora
        response_data = response.json()
        bot_response = response_data["choices"][0]["message"]["content"]

        # Prikažemo odziv modela v komunikatorju
        chat_log.insert(tk.END, f"GPT-4All: {bot_response}\n")
        chat_log.see(tk.END)  # Samodejno pomikamo pogled na zadnje sporočilo

        # Generiramo in predvajamo govor
        audio_file = generate_speech(bot_response)
        if audio_file:
            play_audio(audio_file)
            os.remove(audio_file)  # Po predvajanju izbrišemo datoteko
    except Exception as e:
        bot_response = f"Napaka: {str(e)}"
        chat_log.insert(tk.END, f"GPT-4All: {bot_response}\n")
        chat_log.see(tk.END)

# Ustvarimo glavno aplikacijo
app = tk.Tk()
app.title("GPT-4All Komunikator z Govornikom")

# Komunikator - prikaz pogovora
chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, state="normal", width=60, height=25)
chat_log.pack(padx=10, pady=10)

# Vnosno polje za uporabnika
user_entry = tk.Text(app, height=3, wrap=tk.WORD)
user_entry.pack(padx=10, pady=5)

# Pošlji gumb
send_button = tk.Button(app, text="Pošlji", command=send_message)
send_button.pack(pady=5)

# Zagon Tkinter aplikacije
app.mainloop()

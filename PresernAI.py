import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
import requests
import os
from playsound import playsound  # Za predvajanje MP3 datoteke

# Inicializirajte OpenAI odjemalca z vašim API ključem
client = OpenAI(api_key="APIKLJUC")

# Določite parametre govornik API
govornik_url = "https://s1.govornik.eu"
govornik_voice = "marko"
govornik_source = "PresernAI"
govornik_version = "3"

# Funkcija za pošiljanje uporabniškega vnosa na OpenAI API
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    # Prikaz uporabniškega vnosa v pogovornem oknu
    chat_box.insert(tk.END, "Vi: " + user_input + "\n")
    
    # Klic OpenAI API
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are France Prešeren."},
                {"role": "user", "content": user_input}
            ]
        )
        # Uporabite `.content` za dostop do besedila odgovora
        assistant_response = completion.choices[0].message.content
    except Exception as e:
        assistant_response = f"Napaka: {str(e)}"
    
    # Prikaz odgovora asistenta v pogovornem oknu
    chat_box.insert(tk.END, "Prešeren: " + assistant_response + "\n")
    
    # Klic govornik API za generiranje govora
    try:
        govornik_params = {
            "voice": govornik_voice,
            "text": assistant_response,
            "source": govornik_source,
            "version": govornik_version
        }
        response = requests.post(govornik_url, data=govornik_params)
        if response.status_code == 200:
            # Shranite MP3 datoteko
            mp3_file = "output.mp3"
            with open(mp3_file, "wb") as f:
                f.write(response.content)
            print(f"MP3 datoteka shranjena kot '{mp3_file}'")
            
            # Predvajajte generirano MP3 datoteko
            playsound(mp3_file)
        else:
            print(f"Neuspešno pridobivanje MP3. Statusna koda: {response.status_code}, Odgovor: {response.text}")
    except Exception as e:
        print(f"Napaka pri generiranju govora: {e}")
    
    # Počistite vnosno polje
    input_box.delete("1.0", tk.END)

# Funkcija za predvajanje MP3 datoteke
def play_mp3():
    mp3_file = "output.mp3"  # Zamenjajte s potjo do vaše MP3 datoteke
    os.startfile(mp3_file)

# Ustvarite glavno okno aplikacije
app = tk.Tk()
app.title("Pogovor z Francetom Prešerenom")

# Ustvarite pogovorno okno za prikaz pogovora
chat_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=20, state="normal")
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Ustvarite vnosno polje za uporabnika, da vpiše svoje sporočilo
input_box = tk.Text(app, wrap=tk.WORD, width=50, height=5)
input_box.grid(row=1, column=0, padx=10, pady=10)

# Ustvarite gumb "Pošlji"
send_button = tk.Button(app, text="Pošlji", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Gumb "Predvajaj" za predvajanje zvoka
play_button = tk.Button(app, text="Predvajaj", command=play_mp3, width=10)
play_button.grid(row=1, column=2, padx=10, pady=10)

# Zaženite aplikacijo
app.mainloop()

# PrešerenAI
Cilj projekta je bil ustvariti chatbota, ki se pretvarja, da je France Prešeren in nam odgovarja na vprašanja. Za izvedbo je bil cilj uporabiti LLM model in iz njega pridobiti ustrezne odgovore na razna vprašanja o Francetu Prešrenu.
Projekt sem razdelil v tri sklope. Prvi sklop vsebuje raziskave in testiranje različnih LLM modelov, tako lokalnih kot spletnih. Sledi razvoj programa za povezavo preko API vmesnika in na koncu sledi še dodelava tega API-ja z TTS funkcionalnostjo.



# Potek projekta
Poleg projekta je ideja še nekoliko večja, saj je v načrtu izvedba hologramske osebe, s katero se bo možno pogovarjati. Na spodnji sliki lahko vidite načrt, kako bo zadeva izgledala. V jedru bo program, ki se bo lahko povezal z različnimi spletnimi ali lokalnimi aplikacijami preko API povezave in izmenjeval podatke med njimi. Najprej bo program zajel naš govor in ga predelal v tekst preko STT. Sledil bo LLM model, ki nam bo generiral odgovor. Odgovor se bo poslal na TTS in se shranil v mp3 datoteko. Sledila bo generacija videa osebnosti, ki bo odpirala usta in se premikala glede na prejet posnetek. Na koncu se bo celotna zadeva predvajala v načinu za hologramski video in se pred nami prikazala kot hologram. 
Zaradi časovne omejenosti in zahtevnosti tega projekta se bom omejil le na prevokotnik, ki ga lahko jasno vidite na sliki. Torej izdelal bom aplikacijo, ki komunicira z LLM modelom in TTS preko API in ju tako poveže skupaj v eno.  

![image](https://github.com/user-attachments/assets/bdc94cd4-8b99-4545-812b-abe0f36014e5)


## Faza 1: Raziskava

V tej fazi sem raziskal različna AI orodja in API-je, da bi našel najboljše rešitve za moje potrebe. Sledijo možne izbire:

Gradio (angleščina): Orodje za hitro ustvarjanje uporabniških vmesnikov za strojno učenje.

WSL: Uporabljeno za postavitev lokalnih jezikovnih modelov (LLM), še posebej uporabno pri večjem obsegu dela, vključno s finetuningom.

GPT4all: Odlična platforma za enostavno integracijo lokalnih LLM-ov.

OpenAI ChatGPT API: Zanesljiva platforma za implementacijo in interakcijo z modeli GPT.
Odločil sem se za ChatGPT od Open AI, saj nam ponuje najboljše odgovore na zastavljena vprašanja in odgovarja v lepi slovenščini.
# Favorita:
## Gpt4all
Odlično orodje za izvajanje lokalnih LLM modelov. Omogoča hitro in enostavno implementacijo, veliko izbiro lokalnih LLM modelov, nativen support za GPU in API vmesnik za povezovanje z drugimi aplikacijami.
Link:https://www.nomic.ai/gpt4all
![image](https://github.com/user-attachments/assets/f655d46e-3ca1-429b-af32-1e4ac6ffa47f)


## Open-AI Chat GPT
Plačljiva verzija ChatGPT, ki omogoča povezovanje preko API za prenos teksta, TTS, STT, finetuning gpt modelov in celo pogovor v živo. 


# Faza 2: Vmesnik za API
V tej fazi sem izdelal programsko kodo, ki se poveže preko API na LLM, dobi odgovor in ga prikaže.  Pri fazi 3 pa sem še dodelal program tako, da se poveže še na sentitizator govora in nam vrne govor v .mp3  formatu.
Faza 2 je tudi najbolj obsežna, saj je potrebno veliko časa in dela, da program pravilno deluje in tudi tako kot hočemo.

## 2.1 Izdelava programa, ki se poveže s OpenAI
Prva stvar, ki jo je bilo potrebno urediti je bil nakup OpenAI in pregled API dokumentacije. API dokumentacija: https://platform.openai.com/docs/api-reference/introduction
Za delovanje te kode je potrebno namestiti knjižnico:

```python
pip install openai
```
Nato moramo vnesti lastni API ključ in si izbrati, kater model želimo uporabljati. Več si lahko preberete v dokumentaciji: 
```python
from openai import OpenAI
client = OpenAI(api_key="API_kljuc")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are France Prešeren."},
        {
            "role": "user",
            "content": "Kdo si pa ti?."
        }
    ]
)

print(completion.choices[0].message)


```
Sledilo je dodajanja uporabniškega vmesnika:
```python
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# Inicializirajte OpenAI odjemalca z vašim API ključem
client = OpenAI(api_key="API_kljuc")

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
    
    # Počistite vnosno polje
    input_box.delete("1.0", tk.END)

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

# Zaženite aplikacijo
app.mainloop()
```
Ko dodamo uporabniški vmesnik program izgleda takole:

![image](https://github.com/user-attachments/assets/53b86ddf-bda9-42ca-b96d-091f57ffd606)

# Faza 3: Text v govor TTS (Text to speech)
V zadnji fazi sem dodal še TTS (Text To Speech). Podobno, kot pri izbiri LLM sem sem najprej poiskal, kaj že obstaja in kaj bi lahko uporabil. Odločal sem se med naslednjimi:

## Slovenski sintetizator govora - Govornik
Brezplačen slovenski API za sintetizacijo govora.
Omogoča pretvorbo teksta v mp3 glasovni forma preko GET metode.
Link: https://www.govornik.eu/govornik-api
![image](https://github.com/user-attachments/assets/7541ab8d-5908-4a12-a2b3-2aa25145e1c0)

## Naraket: Kvalitetni, vendar plačljivi sintetizatorji govora za slovenščino
Za več izbire različnih glasov je možno uporabiti tudi druge sintentizatorje govora. Eden izmed njih je npr. narakeet:
Link: https://www.narakeet.com/languages/text-to-speech-slovenian/
![image](https://github.com/user-attachments/assets/761679a7-b541-42f3-8e78-60324bcecb9e)

## Izbira - Govornik
Na koncu sem izbral Govornik, saj je brezplačen in omogoča relativno hitro implementacijo. Najprej sem izdelal program, ki se poveže z Govornikom in nam vrne MP3 zvočni zapis. 
Več lahko izveste o Govorniku na tej povezavi: https://www.govornik.eu/govornik-api 
```python
import requests

# Define the URL and parameters
url = "https://s1.govornik.eu"
params = {
    "voice": "nik-unit",
    "text": "Pozdravljen na ta prekrasen dan. Jaz ti bom povedal da sem ta Janez",
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
```
Govornika sem na koncu še dodal v program in dodal gumb za predvajanje zvočnega posnetka.
```python
import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
import requests
import os
from playsound import playsound  # For playing the MP3 file
import threading
import pygame

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

# Define the govornik API parameters
govornik_url = "https://s1.govornik.eu"
govornik_voice = "marko"
govornik_source = "PresernAI"
govornik_version = "3"

# Function to handle sending user input to the OpenAI API
def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    # Display the user's input in the chat box
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    
    # Call OpenAI API
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are France Prešeren."},
                {"role": "user", "content": user_input}
            ]
        )
        # Use `.content` to access the response text
        assistant_response = completion.choices[0].message.content
    except Exception as e:
        assistant_response = f"Error: {str(e)}"
    
    # Display the assistant's response in the chat box
    chat_box.insert(tk.END, "Assistant: " + assistant_response + "\n")
    
    # Call govornik API to generate speech
    try:
        govornik_params = {
            "voice": govornik_voice,
            "text": assistant_response,
            "source": govornik_source,
            "version": govornik_version
        }
        response = requests.post(govornik_url, data=govornik_params)
        if response.status_code == 200:
            # Save the MP3 file
            mp3_file = "output.mp3"
            with open(mp3_file, "wb") as f:
                f.write(response.content)
            print(f"MP3 file saved as '{mp3_file}'")
            
            # Play the generated MP3 file
            playsound(mp3_file)
        else:
            print(f"Failed to fetch MP3. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error while generating speech: {e}")
    
    # Clear the input box
    input_box.delete("1.0", tk.END)

mp3_file = "output.mp3"
# Function to play the generated audio
def play_audio():
    if os.path.exists(mp3_file):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_file)
            pygame.mixer.music.play()
        except Exception as e:
            chat_box.insert(tk.END, f"Assistant: Error playing audio: {e}\n")
    else:
        chat_box.insert(tk.END, "Assistant: No audio file found. Please generate speech first.\n")


# Create the main application window
app = tk.Tk()
app.title("Chat with France Prešeren")

# Create a chat box to display the conversation
chat_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=20, state="normal")
chat_box.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create an input box for the user to type their message
input_box = tk.Text(app, wrap=tk.WORD, width=50, height=5)
input_box.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(app, text="Send", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# "Play" button to play the audio
play_button = tk.Button(app, text="Play", command=play_audio, width=10)
play_button.grid(row=1, column=2, padx=10, pady=10)

# Run the application
app.mainloop()


```
# Končni Projekt
Na koncu je nastala aplikacija, ki poveže ChatGPT z sintetizatorjem govora Govornik. Ko vpišemo nek tekst ga program pošlje ChatGPTju, ki nam vrne odgovor. Odgovor se izpiše in pošlje Govorniku, ki nam vrne mp3 zvočni posnetek. Ta posnetek pa si nato lahko predvajamo.



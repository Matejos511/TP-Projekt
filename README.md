# PrešerenAI
Cilj projekta je bil ustvariti chatbota, ki se pretvarja, da je France Prešeren in nam odgovarja na vprašanja. Za izvedbo je bilj cilj uporabiti LLM model in iz nejega pridobiti odgovore na razna vprašanja.
Projekt sem razdelil v tri sklope. Prvi sklop je vseboval raziskave in testiranje različnih LLM modelov tako lokalnih, kot spletnih. Sledil je razvoj programa za povezavo preko API vmesnika in na koncu še dodelava tega APIja z TTS funkcionalnostjo.



# Potek projekta
Poleg projekta je ideja še nakoliko većja, saj je v načrtu izvedba hologramske osebe, s katero se bo možno pogovarjati. Na spodnji sliki lahko vidite načrt, kako bo zadeva izgledala. V jedru bo program, ki se bo lahko povezal z različnimi online ali lokalnimi aplikacijami preko API povezave in izmenjeval podatke med njimi. Najprej bo program zajel naš govor in ga predelal v tekst preko STT. Sledil bo LLM model, ki nam bo generiral odgovor. Odgovor se bo poslal na TTS in se shranil v mp3 datoteko.   Sledila bo še generacija videa osebnosti, ki bo odpirala usta in se premikala glede na prejet posnetek. Na koncu se bo celotna zadeva predvajala v načinu za hologramski video in se pred nami prikazala kot hologram. 
Zaradi časovne omejenosti in zahtevnosti tega projekta se bom omejil le na prevokotnik, ki ga lahko jasno vidite na sliki. Torej izdelal bom aplikacijo, ki komunicira z LLM modelom in nato še TTS preko API in ju tako poveže skupaj v eno.  
![image](https://github.com/user-attachments/assets/bdc94cd4-8b99-4545-812b-abe0f36014e5)


## Faza 1: Raziskava

V tej fazi sem raziskal različna AI orodja in API-je, da bi našel najboljše rešitve za moje potrebe. Sledijo možne izbire:

Gradio (angleščina): Orodje za hitro ustvarjanje uporabniških vmesnikov za strojno učenje.

WSL: Uporabljeno za postavitev lokalnih jezikovnih modelov (LLM), še posebej uporabno pri večjem obsegu dela, vključno s finetuningom.

GPT4all: Odlična platforma za enostavno integracijo lokalnih LLM-ov.

OpenAI ChatGPT API: Zanesljiva platforma za implementacijo in interakcijo z modeli GPT.
Odločil sem se za chatGPT od Open AI, saj nam ponuje najboljše odgovore na zastavljena vprašanja in dogovarja v lepi slovenščini.
# Favorita:
## Gpt4all
Odlično orodje za izvajanje lokalnih LLM modelov. Omogoča hitro in enostavno implementacijo, veliko izbiro lokalnih LLM modelov, nativen suport za GPU in API vmesnik za povezvanje z drugimi aplikacijami.
Link:https://www.nomic.ai/gpt4all
![image](https://github.com/user-attachments/assets/f655d46e-3ca1-429b-af32-1e4ac6ffa47f)


## Open-AI Chat GPT
Plačljiva verzija chat GPT, ki omogoča povezovanje preko API za prenos teksta, TTS, STT, finetuning gpt modelov in celo pogovor v živo. 


# Faza 2: Vmesnik za API
V tej fazi sem izdelal programsko kodo, ki se poveže preko API na LLM, dobi odgovor in ga prikaže.  Pri fazi 3 pa sem še dodelal program tako, da se poveže še na sentitizator govora in nam vrne govor v .mp3  formatu.
Faza 2 je tudi najbolj obsežna, saj je potrebno veliko časa in dela, da program pravilno deluje in tudi tako kot hočemo.

## 2.1 Izdelava programa, ki se poveže s OpenAI
Prva stvar, ki jo je bilo potrebno urediti je bil nakup OpenAI in pregled API dokumentacije. API dokumentacija: https://platform.openai.com/docs/api-reference/introduction
Za delovanje te kodeje potrebno namestiti knjižnico:

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

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="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")

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
    chat_box.insert(tk.END, "Preseren: " + assistant_response + "\n")
    
    # Clear the input box
    input_box.delete("1.0", tk.END)

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
send_button = tk.Button(app, text="Send", command=send_message, width=10)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the application
app.mainloop()
```

![image](https://github.com/user-attachments/assets/53b86ddf-bda9-42ca-b96d-091f57ffd606)

# Faza 3: Text v govor TTS (Text to speech)

TTS: Tehnologija pretvorbe besedila v govor

Favoriti za slovensko TTS:

## Slovenski sentitizator govora - Govornik
Brezplačen slovenski API za sintetizacijo govora.
Omogoča pretvorbo teksta v mp3 glasovni forma preko GET metode.
Link: https://www.govornik.eu/govornik-api
![image](https://github.com/user-attachments/assets/7541ab8d-5908-4a12-a2b3-2aa25145e1c0)

## Naraket: Kvalitetni, vendar plačljivi sintetizatorji govora za slovenščino.
Za več izbire različnih glasov je možno uporabiti tudi druge sintentizatorje govora. Eden izmed njih je npr. narakeet:
Link: https://www.narakeet.com/languages/text-to-speech-slovenian/
![image](https://github.com/user-attachments/assets/761679a7-b541-42f3-8e78-60324bcecb9e)

# Končni Projekt
Na koncu je nastala aplikacija, ki poveže chatGPT z sintentizatorjem govora Govornik.


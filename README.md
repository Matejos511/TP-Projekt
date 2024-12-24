# PrešerenAI
Cilj projekta je bil ustvariti chatbota, ki se pretvarja, da je France Prešeren in nam odgovarja na vprašanja. Za izvedbo je bilj cilj uporabiti LLM model in iz nejega pridobiti odgovore na razna vprašanja.
Projekt sem razdelil v tri sklope. Prvi sklop je vseboval raziskave in testiranje različnih LLM modelov tako lokalnih, kot spletnih. Sledil je razvoj programa za povezavo preko API vmesnika in na koncu še dodelava tega APIja z TTS funkcionalnostjo.



# Potek projekta
![image](https://github.com/user-attachments/assets/bdc94cd4-8b99-4545-812b-abe0f36014e5)


## Faza 1: Raziskava

V tej fazi sem raziskal različna AI orodja in API-je, da bi našel najboljše rešitve za moje potrebe. Sledijo možne izbire:

Gradio (angleščina): Orodje za hitro ustvarjanje uporabniških vmesnikov za strojno učenje.

WSL: Uporabljeno za postavitev lokalnih jezikovnih modelov (LLM), še posebej uporabno pri večjem obsegu dela, vključno s finetuningom.

GPT4all: Odlična platforma za enostavno integracijo lokalnih LLM-ov.

OpenAI ChatGPT API: Zanesljiva platforma za implementacijo in interakcijo z modeli GPT.
# Favorita:
## Gpt4all
Odlično orodje za izvajanje lokalnih LLM modelov. Omogoča hitro in enostavno implementacijo, veliko izbiro lokalnih LLM modelov, nativen suport za GPU in API vmesnik za povezvanje z drugimi aplikacijami.
Link:https://www.nomic.ai/gpt4all
![image](https://github.com/user-attachments/assets/f655d46e-3ca1-429b-af32-1e4ac6ffa47f)


## Open-AI Chat GPT
Plačljiva verzija chat GPT, ki omogoča povezovanje preko API za prenos teksta, TTS, STT, finetuning gpt modelov in celo pogovor v živo. 


# Faza 2: Vmesnik za API
V tej fazi sem izdelal programsko kodo, ki se poveže preko API na LLM, dobi odgovor in ga prikaže.  Pri fazi 3 pa sem še dodelal program tako, da se poveže še na sentitizator govora in nam vrne govor v .mp3  formatu.
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


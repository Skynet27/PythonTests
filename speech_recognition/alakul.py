import speech_recognition as sr
from gtts import gTTS
import playsound
import datetime

# va = __import__("my-voice-analysis")

name = "szevasz"
r1 = sr.Recognizer()


def get_background_noise():
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)


def get_audio():
    with sr.Microphone() as source:
        try:
            audio = r1.listen(source, timeout=3)
        except:
            print("(timout)")
            get_audio()
        try:
            return (r1.recognize_google(audio, language="hu-HU")).lower()
        except:
            print("(hiba)")
            return "hiba"


def speak(text):
    tts = gTTS(text=text, lang="hu")
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")


while True:
    #get_background_noise()
    print("Hallgatás...")
    text = get_audio()
    if text.count(name) > 0:
        print("Mit szeretnél?")
        get_background_noise()
        text = get_audio()
        if "semmit" in text:
            print("Akkor hagylak is!")
            speak("Akkor hagylak is!")
        elif "mennyi az idő" in text:
            now = datetime.datetime.now()
            print(f"Most {now.hour} óra {now.minute} perc van.")
            speak(f"Most {now.hour} óra {now.minute} perc van.")
        elif "mondd meg a dátumot" in text:
            now = datetime.datetime.now()
            print(f"Ma {now.year} {now.month} hó {now.day} nap van.")
            speak(f"Ma {now.year} {now.month} hó {now.day} nap van.")
        else:
            print(text)
            print("Nem értettem.")
    elif text == "hiba":
        print("Hiba lépett fel.")

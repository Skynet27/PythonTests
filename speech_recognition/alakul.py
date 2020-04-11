import speech_recognition as sr
from gtts import gTTS
import playsound

# va = __import__("my-voice-analysis")

name = "szevasz"
r1 = sr.Recognizer()


def get_background_noise():
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)


def get_audio():
    with sr.Microphone() as source:
        audio = r1.listen(source)

        try:
            return (r1.recognize_google(audio, language="hu-HU")).lower()
        except:
            return "hiba"


def speak(text):
    tts = gTTS(text=text, lang="hu")
    tts.save("voice.mp3")
    playsound.playsound("voice.mp3")


while True:
    get_background_noise()
    print("Hallgatás...")
    text = get_audio()
    if text.count(name) > 0:
        speak("Mit szeretnél?")
        text = get_audio()
        if "semmit" in text:
            speak("Akkor hagylak is!")
        else:
            speak("Nem értettem.")
    elif text == "hiba":
        print("Hiba lépett fel.")

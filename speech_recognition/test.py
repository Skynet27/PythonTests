import speech_recognition as sr

sa = __import__("my-voice-analysis")

r1 = sr.Recognizer()
r2 = sr.Recognizer()

with sr.Microphone() as source:
    print("Beszélhetsz:")
    audio = r1.listen(source)
    spc = r1.recognize_google(audio, language="hu-HU")
    print(spc)

if (spc.lower() == "szevasssz öcsém") or (spc.lower() == "jarvis"):
    with sr.Microphone() as source:
        print("Mondjad, miaz?")
        audio = r2.listen(source)
        spc = r2.recognize_google(audio, language="hu-HU")
        print("Ezt mondtad: " + spc)
else:
    print("Nem szólítottál meg!")

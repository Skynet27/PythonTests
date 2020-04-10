import speech_recognition as sr
import webbrowser as wb

# va = __import__("my-voice-analysis")

r1, r2, r3 = sr.Recognizer(), sr.Recognizer(), sr.Recognizer()


def main():
    with sr.Microphone() as source:
        try:
            r1.adjust_for_ambient_noise(source)
            print("Beszélhetsz:")
            audio = r1.listen(source)
            scp = r1.recognize_google(audio, language="hu-HU")
            if scp.lower() == "szevasz":
                kuldd(scp)
            else:
                kuldd("Mondd újra:")
        finally:
            kuldd("reapeat")


def kuldd(arg):
    if arg != "repeat":
        print(arg)
        main()
    else:
        main()


main()

import speech_recognition as sr
import webbrowser as wb

va = __import__("my-voice-analysis")

r1, r2, r3 = sr.Recognizer()


def main():
    with sr.Microphone as source:
        print("Beszélhetsz:")
        scp = r1.recognize_google(r1.listen(source))
        if scp == "ágota":
            print("Szia, cicca!")
        main()


main()

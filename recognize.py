import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
engine=engine = pyttsx3.init()
voices = engine.getProperty("voices")

while (True):
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.record(source)

    try:
        text=r.recognize_google(audio, language='ta-In')
        print(text)
        engine.setProperty("voice",voices[1].id)
        engine.say(text)
        engine.runAndWait()
    except:
        print("Sorry could not hear you")



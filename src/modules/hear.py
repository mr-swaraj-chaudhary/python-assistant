import speech_recognition as sr
from .speak import speak

def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)

        try:
            speak("Interpreting...")
            text = r.recognize_google(audio, show_all=False, language="en-US")
            return text
        except sr.RequestError as e:
            speak(f"Failed to request results: {e}")
        except sr.UnknownValueError:
            speak("There was a system failure...")
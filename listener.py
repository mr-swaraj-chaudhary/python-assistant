# module to develop a listener
# uses inbuilt microphone to detect audio
# the audio is then converted to text using google recognizer
import speech_recognition
from speaker import speak


def hear():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            speak("Recognizing...")
            command = recognizer.recognize_google(audio, language="en-in")
        except:
            command = "None"
            print(
                "There was some problem detecting your speech, please say that again...")
            speak(
                "There was some problem detecting your speech, please say that again...")
        finally:
            print(f"What I heard : {command}")
            speak(f"What I heard : {command}")
    return command


hear()

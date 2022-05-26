# module to develop a speaker
# creates an engine using pyttsx3 module and microsoft speech api
# an speaker is created using the generated engine
import pyttsx3

engine = pyttsx3.init("sapi5")
available_voices = engine.getProperty("voices")
engine.setProperty("voice", available_voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

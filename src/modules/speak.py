import pyttsx3

engine = pyttsx3.init("sapi5")
engine.setProperty("voice", 'en-us')
engine.setProperty('rate', 200)

def speak(h_text):
    engine.say(h_text)
    engine.runAndWait()
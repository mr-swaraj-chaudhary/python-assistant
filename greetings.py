# module for greetings
# greets user as per the time

import speak
import datetime


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning, master...")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon master...")
    else:
        speak("Good evening master...")
    speak("My good name is Aarambh and I am responsible for automating your day to day tasks.")
    speak("I hope you'll find me useful.")

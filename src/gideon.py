import os
import datetime
from src.modules.hear import hear
from src.modules.speak import speak

def courtesies():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Sir!")
    else:
        speak("Good Evening, Sir!")
    speak("I am your assistant, What are we up to today?")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    courtesies()
    while True:
        h_text = hear().lower()
        if not h_text: continue
        speak(h_text)
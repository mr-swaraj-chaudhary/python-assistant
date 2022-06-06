from datetime import datetime
from welcome import greetings
from listener import hear
from speaker import speak
import wikipedia
import webbrowser
import os
import random
import smtplib

if __name__ == "__main__":
    greetings()
    while True:
        command = hear().lower()
        if "wikipedia" in command:
            print("Searching wikipedia...")
            speak("Searching wikipedia...")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            speak(results)
        elif "open youtube" in command:
            webbrowser.open_new_tab("https://youtube.com")
        elif "open google" in command:
            webbrowser.open_new_tab("https://google.com")
        elif "open stackoverflow" in command:
            webbrowser.open_new_tab("https://stackoverflow.com")
        elif "open github" in command:
            webbrowser.open_new_tab("https://github.com/Happ2y")
        elif "open linkedin" in command:
            webbrowser.open_new_tab(
                "https://www.linkedin.com/in/swaraj--kumar/")
        elif "open instagram" in command:
            webbrowser.open_new_tab(
                "https://www.instagram.com/swarajkumarchaudhary/")
        elif "open facebook" in command:
            webbrowser.open_new_tab(
                "https://www.facebook.com/swaraj4715/")
        elif "open classroom" in command:
            webbrowser.open_new_tab(
                "https://classroom.google.com/h")
        elif "play music" in command:
            music_directory = "C:\\Users\\blushingHappy\\Music"
            available_songs = os.listdir(music_directory)
            print(available_songs)
            song_index = random.randint(0, len(available_songs))
            os.startfile(
                os.path.join(
                    music_directory, available_songs[song_index]
                )
            )
        elif "time" in command:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"The time is {time}")
            speak(f"The time is {time}")
        elif "open code" in command:
            vsCodePath = "C:\\Users\\blushingHappy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodePath)
        elif "send email" in command:
            sender = "b190040@nitsikkim.ac.in"
            receiver = "nehabharti1729@gmail.com"
            try:
                print("Enter your gmail password :", end=" ")
                speak("Enter your gmail password")
                password = input()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender, password)

                # message = """From: From Person %s
                # To: To Person %s
                # Subject: Sending SMTP e-mail
                # This is a test e-mail message.
                # """ % (sender, receiver)

                server.sendmail(sender, receiver, "Hii")
                print("Successfully sent email")
                speak("Successfully sent email")
            except Exception as e:
                print(e)
                speak("unable to send email")
                print("unable to send email")

        elif "exit" in command or "shut down" in command or "power off" in command:
            print("Shutting down...")
            speak("Shutting down...")
            exit(1)
        else:
            continue

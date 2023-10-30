import pyttsx3
import speech_recognition as sr
import os
import datetime
import wikipedia
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')

try:
    # Attempt to initialize the text-to-speech engine
    engine = pyttsx3.init('sapi5')
except ImportError:
    print('Error: ImportError')
except RuntimeError:
    print('Error: RuntimeError')

# Set the voice for the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user
def wishme():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("Good morning sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon sir.")
    elif 18 <= hour <= 23:
        speak("Good evening sir.")
    else:
        speak("Good night sir")

# Function to recognize speech input
def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said:", query)
        except Exception as e:
            query = ''
    return query

# Main function
if __name__ == "__main__":
    speak('I AM JARVIS. Your personal assistant.')
    wishme()
    
    while True:
        query = takecmd().lower() #type: ignore
        
        if 'search' in query:
            speak("Searching in Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            continue
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            continue
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            continue

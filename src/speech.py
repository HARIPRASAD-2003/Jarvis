import speech_recognition as sr
import pyaudio
import wave
import pyttsx3

import os

def find_file_path(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Example usage
directory_to_search = "src"
file_to_find = "start1.wav"

file_path = find_file_path(directory_to_search, file_to_find)

if file_path:
    print(f"Found {file_to_find} at: {file_path}")
else:
    print(f"{file_to_find} not found in the directory.")

class SpeechRecognition:
    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.alert_sound_file = file_path
        self.text_to_speech = pyttsx3.init()


    def play_alert_sound(self, sound_file=None):
        if sound_file==None:
            sound_file = self.alert_sound_file
        # Load the audio file
        wf = wave.open(sound_file, 'rb') #type: ignore

        # Create an audio player
        audio = pyaudio.PyAudio()
        stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)

        # Play the audio
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Cleanup
        stream.stop_stream()
        stream.close()
        audio.terminate()
    
    def speak(self, text):
        print("Jarvis: ",text)
        self.text_to_speech.say(text)
        self.text_to_speech.runAndWait()

    def recognize_speech(self):
        # self.play_alert_sound(self.alert_sound_file)  # Play the alert sound

        with sr.Microphone() as source:
            print("Adjusting for ambient noise. Please wait...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)  # Adjust for 5 seconds
            recognized_text = ''
            while(True):
                # self.play_alert_sound(self.alert_sound_file)  # Play the alert sound
                print("Say something:")
                # self.recognizer.pause_threshold = 1
                audio = self.recognizer.listen(source)

                try:
                    print("recognize...")
                    recognized_text = self.recognizer.recognize_google(audio, language='en-in')
                    break
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print("Error with the request: {0}".format(e))
                    
        return recognized_text
# from tkinter.tix import Tree
from speech import SpeechRecognition
from nlp_integration import NLPIntegration
from DataStore import DataStore
from Commands import JarvisCommands
from Com_vis import FaceRecognitionModule
from datetime import datetime

class Jarvis:
    def __init__(self) -> None:
        
        # Initialize components
        self.cam = FaceRecognitionModule("src/Images")
        self.sr = SpeechRecognition()
        self.nlp = NLPIntegration()
        self.data_store = DataStore("src/user_data.json")
        self.cmd = JarvisCommands()
        self.sr.play_alert_sound()
        self.user_name = self.cam.recognize_user()
        if not self.user_name:
            self.sr.speak("I am Jarvis, your personal assistant.")
            self.sr.speak("What's your name?")
            self.user_name = self.sr.recognize_speech()
            self.data_store.set(f"{self.user_name}", self.user_name)
            self.sr.speak(f"Nice to meet you, {self.user_name}!")
            self.cam.add_new_face(self.user_name)
        else:
            self.sr.speak(f"Hello, {self.user_name} sir!")
            self.sr.speak("I am Jarvis, your personal assistant.")
        

    def listen_and_recognize(self, state=True):
        result = str(self.sr.recognize_speech()).lower()
        print("Recognized Text:", result)

        # Example NLP tasks
        tokens = self.nlp.tokenize_text(result)
        print("Tokens:", tokens)
        sentiment = self.nlp.analyze_sentiment(result)
        print("Sentiment Analysis:", sentiment)
        entities = self.nlp.named_entity_recognition(result)
        print("Named Entities:", entities)
        if 'jarvis' in tokens:
            if 'sleep' in tokens:
                print("sleep")
                self.sr.speak("ok Sir!")
                return [True,"sleep"]
            elif 'bye' in tokens or 'goodbye' in tokens:
                print("exit")
                self.sr.speak("GoodBye sir!")
                return [False, 'exit']
            elif 'wake' in tokens or 'wakeup' in tokens:
                print("Wakeup")
                self.sr.play_alert_sound()
                return [True,'wakeup']
            elif state:
                print("exe")
                res = self.cmd.execute_command(tokens)
                self.sr.speak(res)
                return [True, "exe"]
            else:
                print("no exe" , "Use command: Wake UP")
                return [True, "continue"]
        else:
            return [True, "continue"]

    def webcam(self):
        self.cam.recognize_faces()

    def wishme(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:
            self.sr.speak("Good morning sir.")
        elif 12 <= hour < 18:
            self.sr.speak("Good afternoon sir.")
        elif 18 <= hour <= 23:
            self.sr.speak("Good evening sir.")
        else:
            self.sr.speak("Good night sir")


if __name__=='__main__':
    app = Jarvis()
    flag = True
    state = True
    while flag:
        # app.webcam()
        # app.cam.add_new_face("HARIPRASAD")
        r = app.listen_and_recognize(state)
        flag, res= r
        if res == 'sleep':
            state = False
        elif res == 'wakeup':
            app.wishme()
            state = True

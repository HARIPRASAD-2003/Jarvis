from click import command
import spacy
from DataStore import DataStore
from EmailSenderApp import EmailSenderUI
from nlp_integration import NLPIntegration
from Com_vis import FaceRecognitionModule
from speech import SpeechRecognition
import pyautogui as pg
class JarvisCommands:
    def __init__(self):
        self.commands = {
            "hello": self.greet,
            "time": self.get_time,
            "search": self.search_wikipedia,
            "add": self.add_cmd,
            "remove": self.remove_cmd,
            "send": self.send_mail,
            # Add more commands and their corresponding functions here
        }
        self.sr = SpeechRecognition()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp_int = NLPIntegration()
        self.cmd = ""
        self.db = DataStore("src/user_data.json")
        self.query = []
        self.cam = FaceRecognitionModule("src/Images")
        print("Cmd")

    def identify_command(self, tokens):
        for cmd in self.commands.keys():
            if cmd in tokens:
                self.cmd = cmd
                break
        if self.cmd not in tokens:
            self.cmd = self.db.get(self.query, "")

    def execute_command(self, command):
        self.cmd = ""
        print("execute")
        self.query = command
        self.identify_command(command)
        print(self.cmd)
        if self.cmd in self.commands:
            return self.commands[self.cmd]()
        elif self.cmd != "":
            return self.cmd
        else:
            return "Command not recognized."

    def greet(self):
        return "Hello, how can I assist you?"

    def get_time(self):
        import datetime
        now = datetime.datetime.now()
        return f"The time is {now.strftime('%H:%M')}"

    def search_wikipedia(self):
        import wikipedia
        # query = self.nlp_int.identify_search_command_and_query(self.cmd)
        # query = self.nlp_int.identify_search_topic(self.query)
        query = self.query
        if 'search' in query:
            query.remove('search')
        if 'about' in query:
            query.remove('about')
        query = ' '.join(query)
        try:
            result = wikipedia.summary(query, sentences=1)
            print(result)
            return f"According to Wikipedia, {result}"
        except Exception as e:
            return f"Sorry, I couldn't find information on {query}. Error: {str(e)}"

    def add_cmd(self):
        if "user" in self.query:
            if self.cam.recognize_user() == "Hariprasad":
                self.sr.speak("Okay sir!")
                return self.add_user()
            else:
                return f"This command is only accessible by Hariprasad!!"
        elif "command" in self.query:
            self.sr.speak("Ok Sir!")
            return self.add_query()
        else:
            return "Command not recognized"
        
    def remove_cmd(self):
        if "user" in self.query:
            if self.cam.recognize_user() == "Hariprasad":
                self.sr.speak("Okay sir!")
                # return self.remove_user()
            else:
                return f"This command is only accessible by Hariprasad!!"
        elif "command" in self.query:
            return self.remove_query()
        return "" 

    def add_user(self):
        self.sr.speak("What's your name?")
        user_name = self.sr.recognize_speech()
        # self.sr.speak(f"Nice to meet you, {user_name}!")
        self.cam.add_new_face(user_name)
        return f"Nice to meet you, {user_name}!"
    
    def remove_user(self):
        self.sr.speak("Which user do you want to remove?")
        user_name = self.sr.recognize_speech()
        res = self.cam.remove_user_images(user_name)
        return res

    def add_query(self):
        self.sr.speak("Say the command you want to add")
        query = self.sr.recognize_speech()
        self.sr.speak("What do you want me to respond?")
        res = self.sr.recognize_speech()
        self.db.set(query,res)
        return "Command added to database"
    
    def remove_query(self):
        self.sr.speak("Say the command you want to remove")
        query = self.sr.recognize_speech()
        self.db.remove(query)
        return "Command removed from database"
    
    def send_mail(self):
        email_sender = EmailSenderUI()
        email_sender.run()
        return "Email sent successfully"

class JarvisMasterCommands(JarvisCommands):
    def __init__(self):
        super().__init__()

    def gesture_mode(self):
        pass
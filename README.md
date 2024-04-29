# Jarvis - Your Personal Assistant

**Jarvis** is a Python-based personal assistant that can assist you with various tasks. It recognizes voice commands and performs actions based on those commands.

## Supported Commands

1. **Sleep Mode**: 
    - `sleep` - This command makes Jarvis enter sleep mode and won't execute any recognized commands.

2. **Shutdown and Wake-up**:
    - `bye` or `goodbye` - Stops Jarvis completely. You'll need to manually restart Jarvis to use it again.
    - `wake` or `wakeup` - Wakes up Jarvis from sleep mode and starts executing user commands.

3. **Greetings**:
    - `hello` - Jarvis responds with a friendly greeting.

4. **Time**:
    - `time` - Jarvis tells you the current time.

5. **Wikipedia Search**:
    - `search [query]` - Jarvis searches the provided query on Wikipedia and returns relevant information.

6. **Face Recognition**:
    - `add user [username]` (Only accessible by Hariprasad) - Adds a new user to face recognition.
    - `remove user [username]` (Only accessible by Hariprasad) - Removes a user from the face recognition database.

7. **Custom Commands**:
    - `add command [command] [response]` - Adds a custom command with a predefined response.
    - `remove command [command]` - Removes a custom command.

8. **Email Sending**:
    - `send email` - Opens an input field using pygame for precise email inputs and sends the email using pyautogui.

## Prerequisites

- Python 3
- Required libraries (wikipedia, pygame, smtplib, etc.)

## Installation

1. Clone the Jarvis repository.

2. Install the required Python libraries:
    ```bash
    pip install SpeechRecognition
    pip install pyaudio
    pip install pyttsx3
    pip install spacy
    pip install nltk
    pip install textblob
    pip install transformers
    pip install torch
    pip install numpy
    pip install pillow
    pip install wikipedia-api
    pip install pygame
    pip install face_recognition
    pip install PyGetWindow
    pip install pyautogui
    ```

## Usage

1. Start Jarvis:
    ```bash
    python src/jarvis.py
    ```

2. Issue voice commands and Jarvis will respond accordingly.

## Contributors

- Hari Prasad
<!-- 
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

You can replace "Your Name" with your actual name and customize the README further as needed. -->
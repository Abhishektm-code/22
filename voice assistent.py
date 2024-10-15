import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def cmd():
    # Listen for commands
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recordedaudio = recognizer.listen(source)
    
    text = ""  # Initialize text variable
    try:
        text = recognizer.recognize_google(recordedaudio, language='en-US')
        text = text.lower()
        print('Your message:', text)

    except Exception as ex:
        print("Could not understand audio, please try again.")
        return  # Exit the function if there's an error

    # Check commands
    if 'chrome' in text:
        a = 'Opening Chrome...'
        engine.say(a)
        engine.runAndWait()
        programName = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([programName])
        
    if 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        engine.say(current_time)
        engine.runAndWait()
        
    if 'play' in text:
        a = 'Opening YouTube...'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
        
    if 'youtube' in text:
        b = 'Opening YouTube...'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('https://www.youtube.com')

# Main loop
while True:
    cmd()
    
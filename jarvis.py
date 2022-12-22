import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.......')
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command=command.replace('alexa', '')
                print(command)
    except:
        pass
    return command
    
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'who are you' in command:
        talk('I am your friend')
    elif'what is your name' in command:
        talk('my name is mim')
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M: %p')
        print(time)
        talk('Current time is'+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache')
    elif 'i love you' in command:
        talk('sorry i have a boyfrined')
    elif 'are you single' in command:
        talk('I am in a relationship with aiman ')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif'hello'in command:
        talk('hiiii')
    elif'hi'in command:
        talk('hello,what can i do for you')
    elif'how are you' in command:
        talk('i am fine,thanks for asking')
    elif'bye' in command:
        quit
    else:
        talk('I did not get it,please it say again.')
while True:
    run_alexa()
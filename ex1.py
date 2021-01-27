#packages imported for use

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# listener class created to listen the commands
# initialising of on signal command "i am your assistant"

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('i am your assistant')
engine.say('what can i do')
engine.runAndWait()

# main function block starts here

def talk(text):
    engine.say(text)
    engine.runAndWait()
  
# Checking for any exceptions here if any  

while True:

    try:
        with sr.Microphone() as source:
            print("ready to listen")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    
    
    #checking for the command given by the user and executing it

    if 'play' in command:
         song = command.replace('play','')
         talk('playing'+ song)
         pywhatkit.playonyt(song)
    elif 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         talk('current time is'+ time)
         print(time)
    elif 'who is' in command:
         person = command.replace('who is','')
         info = wikipedia.summary(person,1)
         talk(info)
    elif 'who are you' in command:
         talk("i am your assistant")
    elif 'single' or 'relationship' in command:
         talk('i am in relationship with internet')
    elif 'quit' in command:
         b=a
    else:
         talk('i did not recognise')

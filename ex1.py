import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('i am your assistant')
engine.say('what can i do')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()
a=10
b=0
while a!=b:

    try:
        with sr.Microphone() as source:
            print("ready to listen")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass

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
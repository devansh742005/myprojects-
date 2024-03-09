
import webbrowser #pip install webbrowser

import pyttsx3 #pip install pyttsx3
import speech_recognition #pip install speechRecognition

import random 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

jokes = [
    "Why don't scientists trust atoms?\nBecause they make up everything!",
    
    "How does a penguin build its house?\nIgloos it together!",
    "Why couldn't the bicycle stand up by itself?\nBecause it was two-tired!",
    "What do you call fake spaghetti?\nAn impasta!",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
    "How does a snowman get around?\nBy riding an 'icicle'!",
    "Why don't skeletons fight each other?\nThey don't have the guts!",
    "What did one hat say to the other?\nStay here, I'm going on ahead!"
    
]





name_user = input("Who is there? ")
speak(name_user)
speak("What do you want? ")
work_user = int(input())

while work_user != 0:
    if work_user == 1:
        speak("1=index 2=whatsapp 3=instagram 4=youtube 5=samvidha 6=buildit 7=spotify 8= give url &7+ = jokes")
    elif work_user == 2:
        speak("whatsapp")
        D = 'https://web.whatsapp.com'
        webbrowser.open(D)
    elif work_user == 3:
        speak("Instagram")
        D = 'https://www.instagram.com'
        webbrowser.open(D)
    elif work_user == 4:
        speak("youtube")
        
        D = 'https://www.youtube.com'
        webbrowser.open(D)
    elif work_user == 5:
        speak("samvidha")
        D = 'https://samvidha.iare.ac.in/index'
        webbrowser.open(D)
    elif work_user == 6:
        speak("open buldit")
        D = 'https://buildit.iare.ac.in/'
        webbrowser.open(D)
    elif work_user == 7:
        speak("opening Spotify")
        D = 'https://www.spotify.com'
        webbrowser.open(D)
    elif work_user ==8:
        speak("opening given url ")
        D =  input()
        webbrowser.open(D)
        
    elif work_user > 8:
        
        D = random.choice(jokes)
        speak(D)
    
    speak("What do you want next? (Enter 0 to exit): ")
    work_user = int(input())
    if(work_user == 0):speak("thankyou")

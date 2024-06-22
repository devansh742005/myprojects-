
import webbrowser #pip install webbrowser
import pyttsx3 #pip install pyttsx3
import speech_recognition #pip install speechRecognition
from pytube import YouTube #pip install pytube
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
link =  input()
yt = YouTube(link)
speak(yt.title)
yd = yt.streams.get_highest_resolution()
yq = yt.streams.get_lowest_resolution()
speak("which resolution")
iny = int(input())

if(iny==0):
       yd.download("C:\\Users\\ADMIN\\Desktop\\python(projects )\\game\\yuy\\")
       speak("highest")
else:
    yq.download("C:\\Users\\ADMIN\\Desktop\\python(projects )\\game\\yuy\\")
    speak("lowest")
    
speak("your welcome ")
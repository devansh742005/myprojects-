import tkinter as tk
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
    

r = tk.Tk()
r.geometry("500x500")
r.title("Youtube downloader")

label = tk.Label(r, text="Youtube downloader", font=('Papyrus', 18))
label.pack(padx=20, pady=20)

entry = tk.Entry(r, width=40)
entry.pack(padx=40, pady=40)

h = entry.get()


entry1 = tk.Entry(r, width=40 , background= "Green")
entry1.pack(padx=40, pady=40)

h1 = entry1.get()

entry3 = tk.Entry(r, width=40 , background="Red")
entry3.pack(padx=40, pady=40)

h3= entry3.get()

entry2 = tk.Entry(r, width=40 , background="Pink")
entry2.pack(padx=40, pady=40)
h2= entry2.get()
entryq= tk.Entry(r, width=40 ,background="Blue")
entryq.pack(padx=40, pady=40)
hq= entryq.get()
tl = [h , h1 ,h2 , h3 , hq] 
text = tk.Text(r,  height= 69 , width= 69 , text= "IARE Best engineering college", font=('Papyrus', 18),)
text.pack(padx=40, pady=40)



r.mainloop()




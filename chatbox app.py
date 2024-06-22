import tkinter as tk
import webbrowser
from pytube import YouTube
import pyttsx3
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

jokes1 = [
    "Why don't scientists trust atoms?\nBecause they make up everything!",
    "How does a penguin build its house?\nIgloos it together!",
    "Why couldn't the bicycle stand up by itself?\nBecause it was two-tired!",
    "What do you call fake spaghetti?\nAn impasta!",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
    "How does a snowman get around?\nBy riding an 'icicle'!",
    "Why don't skeletons fight each other?\nThey don't have the guts!",
    "What did one hat say to the other?\nStay here, I'm going on ahead!"
]



def download_best_memory():
   
    link = entry.get()
    yt = YouTube(link)
    yd = yt.streams.get_lowest_resolution()
    speak("Downloading lowest resolution video.")
    yd.download("C:\\Users\\ADMIN\\Desktop\\Videos")
    speak("Download complete.")

def index():
    
    speak("1=index 2=whatsapp 3=instagram 4=youtube 5=samvidha 6=buildit 7=spotify 8= give url &7+ = jokes")

def wa():
    
    speak("whatsapp")
    D = 'https://web.whatsapp.com'
    webbrowser.open(D)

def ig():
    
    speak("Instagram")
    D = 'https://www.instagram.com'
    webbrowser.open(D)

def yt():
   
    speak("youtube")
    D = 'https://www.youtube.com'
    webbrowser.open(D)

def iare():
   
    speak("iare")
    D = 'https://samvidha.iare.ac.in/index'
    webbrowser.open(D)

def iarelabs():
   
    speak("iarelabs ")
    D = 'https://buildit.iare.ac.in/'
    webbrowser.open(D)

def spotify():
   
    speak("opening Spotify")
    D = 'https://www.spotify.com'
    webbrowser.open(D)

def close():
    speak("closing")
    r.destroy()

def given_url():
    speak("opening brave")
    D = entry.get()
    webbrowser.open(D)

def jokes():
    D = random.choice(jokes1)
    speak(D)



r = tk.Tk()
r.geometry("500x500")
r.title("chat box")
label = tk.Label(r, text="Chatbox", font=('Papyrus', 18))
label.pack(padx=20, pady=20)

label1 = tk.Label(r, text="place ur URl down \|/", font=('Papyrus', 10))
label1.pack(padx=20, pady=20)

entry = tk.Entry(r, width=40)
entry.pack(padx=40, pady=40)

button_frame = tk.Frame(r)
button_frame.pack(pady=20)

btn1 = tk.Button(button_frame, text="1", font=('Papyrus', 18), command=index)
btn1.grid(row=0, column=0)

btn2 = tk.Button(button_frame, text="2", font=('Papyrus', 18), command=wa)
btn2.grid(row=0, column=1)

btn3 = tk.Button(button_frame, text="3", font=('Papyrus', 18), command=ig)
btn3.grid(row=0, column=2)

btn4 = tk.Button(button_frame, text="4", font=('Papyrus', 18), command=yt)
btn4.grid(row=0, column=3)

btn5 = tk.Button(button_frame, text="5", font=('Papyrus', 18), command=iare)
btn5.grid(row=0, column=4)

btn6 = tk.Button(button_frame, text="6", font=('Papyrus', 18), command=iarelabs)
btn6.grid(row=1, column=0)

btn7 = tk.Button(button_frame, text="7", font=('Papyrus', 18), command=given_url)
btn7.grid(row=1, column=1)

btn8 = tk.Button(button_frame, text="8", font=('Papyrus', 18), command=spotify)
btn8.grid(row=1, column=2)

btn9 = tk.Button(button_frame, text="9", font=('Papyrus', 18), command=download_best_memory)
btn9.grid(row=1, column=3)

btn0 = tk.Button(button_frame, text="0", font=('Papyrus', 18), command=close)
btn0.grid(row=1, column=4)

button_frame.pack()

r.mainloop()

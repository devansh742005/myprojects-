import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import webbrowser
from pytube import YouTube
import pyttsx3
import random
import os
import pygame
from threading import Thread

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def download_best_quality():
    try:
        link = entry.get()
        yt = YouTube(link)
        yd = yt.streams.get_highest_resolution()
        speak("Downloading highest resolution video.")
        yd.download("C:\\Users\\ADMIN\\Desktop\\Videos")
        speak("Download complete.")
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

def open_url(url):
    try:
        speak("Opening browser")
        webbrowser.open(url)
    except Exception as e:
        speak(f"An error occurred: {str(e)}")

def tell_joke():
    D = random.choice(jokes1)
    speak(D)

def browse_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Video File", filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
    if file_path:
        speak("Selected video file: " + file_path)
        # You can perform operations with the selected video file here

def play_background_video():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("C:\\Users\\ADMIN\\Videos\\JARVIS live wallpaper.mp4")
    pygame.mixer.music.play(-1)  # -1 makes the video loop indefinitely

def create_gui():
    global entry
    r = tk.Tk()
    r.geometry("800x600")
    r.title("Chat box")

    # Play background video in a separate thread
    bg_video_thread = Thread(target=play_background_video)
    bg_video_thread.daemon = True
    bg_video_thread.start()

    label1 = tk.Label(r, text=r"place ur URl down \|/", font=('Papyrus', 10))
    label1.pack(pady=10)

    entry = tk.Entry(r, width=40)
    entry.pack(pady=10)

    button_frame = tk.Frame(r)
    button_frame.pack(pady=20)

    btn1 = tk.Button(button_frame, text="1", font=('Papyrus', 18), command=index)
    btn1.grid(row=0, column=0)

    btn2 = tk.Button(button_frame, text="2", font=('Papyrus', 18), command=lambda: open_url('https://web.whatsapp.com'))
    btn2.grid(row=0, column=1)

    btn3 = tk.Button(button_frame, text="3", font=('Papyrus', 18), command=lambda: open_url('https://www.instagram.com'))
    btn3.grid(row=0, column=2)

    btn4 = tk.Button(button_frame, text="4", font=('Papyrus', 18), command=lambda: open_url('https://www.youtube.com'))
    btn4.grid(row=0, column=3)

    btn5 = tk.Button(button_frame, text="5", font=('Papyrus', 18), command=lambda: open_url('https://samvidha.iare.ac.in/index'))
    btn5.grid(row=0, column=4)

    btn6 = tk.Button(button_frame, text="6", font=('Papyrus', 18), command=lambda: open_url('https://buildit.iare.ac.in/'))
    btn6.grid(row=1, column=0)

    btn7 = tk.Button(button_frame, text="7", font=('Papyrus', 18), command=given_url)
    btn7.grid(row=1, column=1)

    btn8 = tk.Button(button_frame, text="8", font=('Papyrus', 18), command=lambda: open_url('https://www.spotify.com'))
    btn8.grid(row=1, column=2)

    btn9 = tk.Button(button_frame, text="9", font=('Papyrus', 18), command=download_best_quality)
    btn9.grid(row=1, column=3)

    btn0 = tk.Button(button_frame, text="0", font=('Papyrus', 18), command=close)
    btn0.grid(row=1, column=4)

    browse_btn = tk.Button(r, text="Browse Video", font=('Papyrus', 18), command=browse_file)
    browse_btn.pack(pady=10)

    # Load the GIF
    image_path = os.path.join("C:", "Users", "ADMIN", "Desktop", "python(projects)", "game", "yuy", "200.gif")
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300), Image.ANTIALIAS)
        gif_img = ImageTk.PhotoImage(img)

        gif_label = tk.Label(r, image=gif_img)
        gif_label.image = gif_img
        gif_label.pack(pady=10)

    button_frame.pack()

    r.mainloop()

def index():
    speak("Index")

def given_url():
    speak("Opening browser")
    D = entry.get()
    webbrowser.open(D)

def close():
    speak("Closing")
    pygame.mixer.music.stop()  # Stop the background video
    r.destroy()

if __name__ == "__main__":
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

    create_gui()

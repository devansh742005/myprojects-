import random
import speech_recognition as sr
import pyttsx3
import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.display.set_mode((1, 1))  # Initialize video system
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    pygame.event.wait()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Enter the number of players: ")
num_players = int(input())

while num_players <= 6:
    playernames = []
    b = 15
    c = num_players

    while c != 1:
        if b == 15:
            for i in range(num_players):
                player_name = input("Enter player name: ")
                playernames.append(player_name)

            print(playernames[:])

        audio_file_path = r'C:\Users\ADMIN\Desktop\yuy\q.mp3'  # Fix: Added 'r' for raw string

        if c == 6:
            q = random.randint(0, c-1)
            w = playernames.pop(q)
            play_audio(audio_file_path)
            speak(w)
            speak("has been killed")
            print(playernames[:])

        elif 2 <= c <= 5:
            q = random.randint(0, c-1)
            w = playernames.pop(q)
            play_audio(audio_file_path)
            speak(w)
            speak("has been killed")
            print(playernames[:])

        elif c == 1:
            speak("The winner is")
            speak(playernames[0])
            num_players = 8
            break

        c -= 1
        b = c

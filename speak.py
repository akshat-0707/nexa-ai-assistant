from gtts import gTTS
import pygame
import os

pygame.mixer.init()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    # Initialize pygame mixer
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    #keep the program running till music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
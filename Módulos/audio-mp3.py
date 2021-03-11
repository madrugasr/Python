#Tocando uma musica MP3.

import pygame

print("MÚSICA MP3")

pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
pygame.event.wait()

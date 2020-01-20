'''
Faça um programa em Python que abra e reproduza o áudio de um aquivo MP3.

Rafael Bispo
13/01/2020
'''
import pygame

pygame.init()
pygame.mixer.init(44100)
pygame.mixer.music.load('Queen - We Are The Champions.mp3')
pygame.mixer.music.play()
#pygame.fadeout(2000)
pygame.event.wait()



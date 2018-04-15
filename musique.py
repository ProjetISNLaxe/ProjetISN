import pygame
from pygame.locals import *
from shooter_fonction import *
from perso_classes import *
from map import *
from pygame import *
from option import *
from sys import exit

def musiquerpg():
    pygame.mixer.music.load("musique/RPG1.wav")
    pygame.mixer.music.play(loops=0, start=0.0)


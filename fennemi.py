import pygame
from pygame.locals import *
from random import *
import time
from classes_tpt import *
from affichage import *


def cible():  # le type de l'ennemi et ses attaques
    if not sinatra.active:
        n = [1, 2]
    else:
        n = [1, 2, 3]
    if david.vie == 0:
        n[1] = 0
    if perso_joueur.vie == 0:
        n[0] = 0
    if sinatra.vie == 0 and sinatra.active:
        n[2] = 0
    p = choice(n)
    while p == 0:
        p = choice(n)
    return p


def verification():
    if david.vie <= 0:
        david.alive = False
        david.vie = 0
    if perso_joueur.vie <= 0:
        perso_joueur.alive = False
        perso_joueur.vie = 0
    if sinatra.vie <= 0:
        sinatra.alive = False
        sinatra.vie = 0
    if sinatra.active:
        if sinatra.vie == 0 and david.vie == 0 and perso_joueur.vie == 0:
            pygame.quit()
            exit()
    elif david.vie == 0 and perso_joueur.vie == 0:
        pygame.quit()
        exit()


def ennemiloup():
    p = cible()
    d = randint(35, 50)
    if p == 2 or david.taunt < 0:
        david.vie -= (d - david.armure)
    elif p == 1:
        perso_joueur.vie -= (d - perso_joueur.armure)
    elif p == 3:
        if random() <= 0.5:
            sinatra.vie -= d
    affichageanimennemi(d, p)
    verification()

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from shooter_fonction import *
from perso_classes import *
from map import *
from combatV3 import *
from pygame import *
from option import *
from sys import exit

devmode = False

pygame.init()
clock = pygame.time.Clock()
fullscreen = open("option/fullscreen", "r")
fullscreenread = fullscreen.read()
fullscreen.close()
if fullscreenread == "0":
    fenetre = pygame.display.set_mode((800, 600))
else:
    fenetre = pygame.display.set_mode((800, 600), FULLSCREEN)
pygame.display.set_caption("Retravel")
icon = pygame.image.load("logo.png").convert_alpha()
pygame.display.set_icon(icon)
fond = []
for i in range(0, 19):
    if i < 10:
        nomimage = "launcher\sprite_menuanimation0" + str(i) + ".png"
    else:
        nomimage = "launcher\sprite_menuanimation" + str(i) + ".png"
    fond.append(pygame.image.load(nomimage).convert())
nfond = 0
x = 0
y = 0

test = pygame.image.load("launcher\pixelgitan.png").convert_alpha()
mask = pygame.mask.from_surface(test)

bouton0 = pygame.image.load("launcher\sprite_boutons0.png").convert_alpha()
bouton0mask = pygame.mask.from_surface(bouton0)
bouton1 = pygame.image.load("launcher\sprite_boutons1.png").convert_alpha()
bouton1mask = pygame.mask.from_surface(bouton1)
bouton2 = pygame.image.load("launcher\sprite_boutons2.png").convert_alpha()
bouton2mask = pygame.mask.from_surface(bouton2)
boutonvierge = pygame.image.load("launcher\sprite_bouton vierge.png").convert_alpha()
lisere = pygame.image.load("launcher\sprite_boutonliseret.png").convert_alpha()
glitch = False
if devmode:
    glitch = True
clique = 0

while 1:
    save = open("save1/save", "r")
    passshooter = int(save.read())
    save.close()
    for event in pygame.event.get():
        if event.type == QUIT:  # pour pouvoir quitter le jeux
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # les deplacements
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == MOUSEMOTION:  # Si mouvement de souris
            x = event.pos[0]
            y = event.pos[1]
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if clique == 1:
                tourpartour(fenetre)

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if clique == 2:
                endless(fenetre, glitch)
        if event.type == MOUSEBUTTONUP and event.button == 1:
            if clique == 3:
                option(fenetre)

    if nfond < 30:
        fenetre.blit(fond[0], (0, 0))
    elif nfond < 60:
        fenetre.blit(fond[1], (0, 0))
    elif nfond < 90:
        fenetre.blit(fond[2], (0, 0))
    elif nfond < 120:
        fenetre.blit(fond[3], (0, 0))
    elif nfond < 150:
        fenetre.blit(fond[4], (0, 0))
    elif nfond < 180:
        fenetre.blit(fond[5], (0, 0))
    elif nfond < 210:
        fenetre.blit(fond[6], (0, 0))
    elif nfond < 240:
        fenetre.blit(fond[7], (0, 0))
    elif nfond < 270:
        fenetre.blit(fond[8], (0, 0))
    elif nfond < 300:
        fenetre.blit(fond[9], (0, 0))
    elif nfond < 330:
        fenetre.blit(fond[10], (0, 0))
    elif nfond < 360:
        fenetre.blit(fond[11], (0, 0))
    elif nfond < 390:
        fenetre.blit(fond[12], (0, 0))
    elif nfond < 420:
        fenetre.blit(fond[13], (0, 0))
    elif nfond < 450:
        fenetre.blit(fond[14], (0, 0))
    elif nfond < 480:
        fenetre.blit(fond[15], (0, 0))
    elif nfond < 510:
        fenetre.blit(fond[16], (0, 0))
    elif nfond < 540:
        fenetre.blit(fond[17], (0, 0))
    elif nfond < 570:
        fenetre.blit(fond[18], (0, 0))
    nfond += 1
    if nfond == 571:
        nfond = 0
    fenetre.blit(bouton0, (250, 300))
    fenetre.blit(bouton1, (250, 400))
    fenetre.blit(bouton2, (250, 500))
    rect = (x, y)
    offset_x = 250 - x
    offset_y0 = 300 - y
    offset_y1 = 400 - y
    offset_y2 = 500 - y
    if mask.overlap(bouton0mask, (offset_x, offset_y0)):
        fenetre.blit(lisere, (246, 297))
        clique = 1
    elif mask.overlap(bouton1mask, (offset_x, offset_y1)):
        fenetre.blit(lisere, (246, 397))
        clique = 2
    elif mask.overlap(bouton2mask, (offset_x, offset_y2)):
        fenetre.blit(lisere, (246, 497))
        clique = 3
    else:
        clique = 0

    clock.tick(60)
    pygame.display.flip()

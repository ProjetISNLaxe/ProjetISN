#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from shooter_fonction import *
from perso_classes import *
from map import *
from pygame import *
from option import *
from sys import exit
from imageinterfacetoload import *

def arbre_compet(fenetre):
    chargementsauvegarde()
    fond = pygame.image.load("inventory/fond.jpg").convert()
    bouclier = pygame.image.load("competance/bouclier.png").convert_alpha()
    boucliermask = pygame.mask.from_surface(bouclier)
    coeur = pygame.image.load("competance/coeur.png").convert_alpha()
    coeurmask = pygame.mask.from_surface(coeur)
    degat = pygame.image.load("competance/degat.png").convert_alpha()
    degatmask = pygame.mask.from_surface(degat)
    mana = pygame.image.load("competance/mana.png").convert_alpha()
    manamask = pygame.mask.from_surface(mana)
    poison = pygame.image.load("competance/poison.png").convert_alpha()
    poisonmask = pygame.mask.from_surface(poison)

    test = pygame.image.load("launcher\pixelgitan.png").convert_alpha()
    mask = pygame.mask.from_surface(test)
    clock = pygame.time.Clock()
    perso="joueur"
    boite=pygame.image.load("inventory/boitetexte.png").convert_alpha()
    x=0
    y=0

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
                if event.key == K_TAB:
                        return
            if event.type == MOUSEMOTION:  # Si mouvement de souris
                x = event.pos[0]
                y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if clique == 1 and perso_joueur.ptdecompetance>=1:
                    perso_joueur.ptdecompetance-=1
                    perso_joueur.ptmana+=1
                if clique == 2 :
                    if perso=="joueur":
                        perso_joueur.ptdecompetance -= 1
                        perso_joueur.ptvie += 1
                    elif perso=="david":
                        david.ptdecompetance -= 1
                        david.ptvie += 1
                    elif perso=="sinatra":
                        sinatra.ptdecompetance -= 1
                        sinatra.ptvie += 1
                if clique == 3:
                    if perso=="joueur":
                        perso_joueur.ptdecompetance -= 1
                        perso_joueur.ptforce += 1
                    elif perso=="david":
                        david.ptdecompetance -= 1
                        david.ptforce += 1
                    elif perso=="sinatra":
                        sinatra.ptdecompetance -= 1
                        sinatra.ptforce += 1
                if clique == 4 and david.ptdecompetance>=3:
                    david.ptdecompetance -= 3
                    david.ptbouclier += 1
                if clique == 5 and sinatra.ptdecompetance>=2:
                    siantra.ptdecompetance -= 2
                    sinatra.ptpoison += 1
                if clique == 6:
                    perso = "joueur"
                if clique == 7:
                    perso = "david"
                if clique == 8 and sinatra.active==True:
                    perso = "sinatra"
        fenetre.blit(fond, (0, 0))
        fenetre.blit(boite, (265, 150))
        if perso=="joueur":
            offset_y = 300 - y
            fenetre.blit(mana, (320, 300))
            fenetre.blit(coeur, (400, 300))
            fenetre.blit(degat, (480, 300))
            fenetre.blit(police.render(str(perso_joueur.ptdecompetance), False, (40, 191, 188)), (95, 10))
            fenetre.blit(police.render(str(perso_joueur.ptmana), False, (0, 0, 188)), (325, 280))
            fenetre.blit(police.render(str(perso_joueur.ptvie), False, (0, 0, 188)), (405, 280))
            fenetre.blit(police.render(str(perso_joueur.ptforce), False, (0, 0, 188)), (485, 280))
            if mask.overlap(manamask, (320-x, offset_y)):
                clique=1
            elif mask.overlap(coeurmask, (400-x, offset_y)):
                clique = 2
            elif mask.overlap(degatmask, (480-x, offset_y)):
                clique = 3
            elif mask.overlap(manamask, (-100000, offset_y-100000)):
                clique = 7
            elif mask.overlap(poisonmask, (-100000, offset_y-100000)):
                clique = 8
            else:
                clique = 0
        elif perso=="david":
            offset_y = 300 - y
            fenetre.blit(bouclier, (320, 300))
            fenetre.blit(coeur, (400, 300))
            fenetre.blit(degat, (480, 300))
            fenetre.blit(police.render(str(david.ptdecompetance), False, (40, 191, 188)), (95, 10))
            fenetre.blit(police.render(str(david.ptbouclier), False, (0, 0, 188)), (325, 280))
            fenetre.blit(police.render(str(david.ptvie), False, (0, 0, 188)), (405, 280))
            fenetre.blit(police.render(str(david.ptforce), False, (0, 0, 188)), (485, 280))
            if mask.overlap(boucliermask, (320-x, offset_y)):
                clique = 4
            elif mask.overlap(coeurmask, (400-x, offset_y)):
                clique = 2
            elif mask.overlap(degatmask, (480-x, offset_y)):
                clique = 3
            elif mask.overlap(manamask, (-100000, offset_y-100000)):
                clique = 6
            elif mask.overlap(poisonmask, (-100000, offset_y-10000)):
                clique = 8
            else:
                clique = 0
        elif perso=="sinatra":
            offset_y = 300 - y
            fenetre.blit(poison, (320, 300))
            fenetre.blit(coeur, (400, 300))
            fenetre.blit(degat, (480, 300))
            fenetre.blit(police.render(str(sintra.ptdecompetance), False, (40, 191, 188)), (95, 10))
            fenetre.blit(police.render(str(sinatra.ptmana), False, (0, 0, 188)), (325, 280))
            fenetre.blit(police.render(str(sinatra.ptvie), False, (0, 0, 188)), (405, 280))
            fenetre.blit(police.render(str(sinatra.ptforce), False, (0, 0, 188)), (485, 280))
            if mask.overlap(poisonmask, (320-x, offset_y)):
                clique = 5
            elif mask.overlap(coeurmask, (400-x, offset_y)):
                clique = 2
            elif mask.overlap(degatmask, (480-x, offset_y)):
                clique = 3
            elif mask.overlap(manamask, (-100000, offset_y-100000)):
                clique = 6
            elif mask.overlap(poisonmask, (-100000, offset_y-100000)):
                clique = 7
            else:
                clique = 0



        clock.tick(60)
        pygame.display.flip()

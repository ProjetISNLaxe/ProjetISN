import pygame
from imageinterfacetoload import *
from pygame.locals import *
from sys import exit
from random import randint
import quete


def dialogue(fenetre, pnj):
    activefich = open("quetes\\pnjrencontre", "w")
    activefich.write(pnj)
    activefich.close()

    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
    textefi = open("pnj/" + pnj + "/dialogue", "r")
    textli = textefi.read().split(";")
    textefi.close()
    imagepnj = pygame.image.load("pnj/" + pnj + "/" + pnj + "_tall.png").convert_alpha()
    bouton1 = pygame.image.load("quetes/HUD/boutonminijeu.png").convert_alpha()
    bouton2 = pygame.image.load("quetes/HUD/boutonquest.png").convert_alpha()
    bouton1rect = bouton1.get_rect()
    bouton2rect = bouton2.get_rect()
    bouton1rect.x = 100
    bouton1rect.y = 545
    bouton2rect.x = 420
    bouton2rect.y = 545
    quetedispof = open("quetes/quetedispo", "r")
    quetedispo = quetedispof.read().split(",")
    quetedispof.close()
    quetefi = open("quetes/active", "r")
    queteactive = quetefi.read()
    quetefi.close()
    if queteactive==pnj:
        quete.quetes(fenetre)
    taillepnj = imagepnj.get_size()
    x = 0
    tobreak = False
    text = textli[randint(0, len(textli) - 1)]
    i = 0
    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type== MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:

                    if testrect.colliderect(bouton1rect):
                        quete.snake(fenetre)
                    if testrect.colliderect(bouton2rect) and pnj in quetedispo:
                        affichquete(fenetre, pnj)
        tobreak = False
        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1]))
        if pnj in quetedispo:
            fenetre.blit(bouton2, bouton2rect)
        fenetre.blit(bouton1, bouton1rect)
        if len(text) > 65:
            affich = []
            k = 0
            motablit = text.split(" ")
            for i in range(int(len(text) / 65) + 3):

                affich.append("")
                while len(affich[i]) < 65:
                    if k < len(motablit) - 1:
                        if len(affich[i] + motablit[k] + " ") < 65:
                            affich[i] += motablit[k] + " "
                        else:
                            break
                        k += 1
                    else:
                        break
            if motablit[-1] not in affich[-1]:
                for i in range(len(alphabet)):
                    for j in range(len(affich)):
                        if alphabet[i] not in affich[j]:
                            affich[j] += motablit[-1]
                            tobreak = True
                            break
                    if tobreak:
                        break
            if len(affich) <= 10:
                for i in range(len(affich)):
                    dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, 10 + 15 * i))
            else:

                tkey = pygame.key.get_pressed()
                if tkey[K_UP] and x + 374 + 15 * len(affich) + 25 > 550:

                    x -= 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                elif tkey[K_DOWN] and 384 + x + 10 <= 384:
                    x += 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                for i in range(len(affich)):
                    if x + 384 + 15 * i < 530:
                        dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, x + 10 + 15 * i))

        if len(text) < 65:
            dialoguequete.blit(police.render(text, True, (32, 153, 152)), (175, 10 + 15 * i))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()

def affichquete(fenetre, pnj):

    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
    textefi = open("quetes/" + pnj + "/objectif", "r")
    text = textefi.read()
    textefi.close()
    quetedispof=open("quetes/quetedispo", "r")
    quetedispo=quetedispof.read().split(",")
    quetedispof.close()
    quetefi = open("quetes/liste", "r")
    queteli=quetefi.read()
    quetefi.close()
    imagepnj = pygame.image.load("pnj/" + pnj + "/" + pnj + "_tall.png").convert_alpha()
    bouton1 = pygame.image.load("quetes/HUD/boutonaccepter.png").convert_alpha()
    bouton2 = pygame.image.load("quetes/HUD/boutonrefuser.png").convert_alpha()
    bouton1rect = bouton1.get_rect()
    bouton2rect = bouton2.get_rect()
    bouton1rect.x = 100
    bouton1rect.y = 545
    bouton2rect.x = 420
    bouton2rect.y = 545
    quetefi = open("quetes/active", "r")
    queteactive = quetefi.read()
    quetefi.close()

    taillepnj = imagepnj.get_size()
    x = 0
    tobreak = False

    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type == MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if testrect.colliderect(bouton2rect):
                        return
                    if testrect.colliderect(bouton1rect):
                        quetefi = open("quetes/liste", "r")
                        queteli=quetefi.read().split(",")
                        quetefi.close()
                        if pnj not in  queteli and pnj in quetedispo:
                            quetefi = open("quetes/liste", "a")
                            quetefi.write("," + pnj)
                            quetefi.close()
                            return


                        if pnj not in queteactive and pnj in queteli:
                            quetefi = open("quetes/active", "w")
                            quetefi.write(pnj)
                            quetefi.close()
                            return





        tobreak = False
        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1]))

        if pnj in queteli and pnj not in queteactive:
            bouton1 = pygame.image.load("quetes/HUD/boutonactiver.png").convert_alpha()
            bouton2=pygame.image.load("quetes/HUD/boutonretour.png").convert_alpha()
            fenetre.blit(bouton1, bouton1rect)
        if pnj in queteli and pnj in queteactive:
            bouton2=pygame.image.load("quetes/HUD/boutonretour.png").convert_alpha()
        if pnj in quetedispo and pnj not in queteli:
            bouton1 = pygame.image.load("quetes/HUD/boutonaccepter.png").convert_alpha()
            bouton2 = pygame.image.load("quetes/HUD/boutonrefuser.png").convert_alpha()
            fenetre.blit(bouton1, bouton1rect)
        fenetre.blit(bouton2, bouton2rect)

        if len(text) > 65:

            affich = []
            k = 0
            motablit = text.split(" ")
            for i in range(int(len(text) / 65) + 3):

                affich.append("")
                while len(affich[i]) < 65:
                    if k < len(motablit) - 1:
                        if len(affich[i] + motablit[k] + " ") < 65:
                            affich[i] += motablit[k] + " "
                        else:
                            break
                        k += 1
                    else:
                        break
            if motablit[-1] not in affich[-1]:
                for i in range(len(alphabet)):
                    for j in range(len(affich)):
                        if alphabet[i] not in affich[j]:
                            affich[j] += motablit[-1]
                            tobreak = True
                            break
                    if tobreak:
                        break

            if len(affich) <= 10:
                for i in range(len(affich)):
                    dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, 10 + 15 * i))
            else:

                tkey = pygame.key.get_pressed()
                if tkey[K_UP] and x + 374 + 15 * len(affich) + 25 > 550:

                    x -= 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                elif tkey[K_DOWN] and 384 + x + 10 <= 384:
                    x += 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                for i in range(len(affich)):
                    if x + 384 + 15 * i < 530:
                        dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, x + 10 + 15 * i))
        if len(text) < 65:
            dialoguequete.blit(police.render(text, True, (32, 153, 152)), (175, 15))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()

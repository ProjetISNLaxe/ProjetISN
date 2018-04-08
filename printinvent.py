import pygame
from pygame.locals import*
from sys import exit
from imageinterfacetoload import *
def printinvent(fenetre):
    clock = pygame.time.Clock()
    fond = pygame.image.load("inventory/fond.jpg").convert()
    follow = False
    curseurrect.x=769
    curseurrect.y=145
    inventairefi=open("save1/inventaire", "r")
    objetinventaireimage = []
    inventairestr=inventairefi.read().split(",")
    for i in range(10):
        objetinventaireimage.append(pygame.image.load("inventory/objetinventaire.png").convert_alpha())
        objetinventairerect.append(Rect(287, 160 + 99 * i, 461,98 ))
    bandeauhaut = pygame.image.load("inventory/bandeaumoney+quete.png").convert_alpha()
    inventairefi.close()
    inventaire=[]
    for i in range (len(inventairestr)):
        inventaire.append([inventairestr[i]])
        for j in range (len(inventaire)):
            fi=open("save1/objet/"+inventaire[i][0], "r")
            inventaire[i].append(int(fi.read()))
            fi.close()
    for i in range (len(inventaire)):
        inventaire[i][0]=pygame.image.load("inventory/objets/"+inventaire[i][0]+".png").convert_alpha()
    quetefi = open("quetes/active", "r")
    queteactive=quetefi.read()
    queteactive =queteactive.capitalize()
    inventairemask=[]
    inventairerect=[]
    for i in range (len(inventaire)):
        inventairemask.append(pygame.mask.from_surface(inventaire[i][0]))
    quetefi.close()
    if queteactive != "":
        missionfi=open("quetes/"+queteactive+"/toprint")
        mission=missionfi.read()
        missionfi.close()
    orfi=open("save1/invent/cpic", "r")
    stror=orfi.read()
    orfi.close()
    lior=list(stror)
    lior.reverse()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_i:
                    return
                if event.key == K_DOWN and curseurrect.y<558:
                    curseurrect.y += 99/1.5
                    for i in range (len(objetinventairerect)):
                        objetinventairerect[i][1]-=98


                if event.key == K_UP and objetinventairerect[0][1]<160:
                    curseurrect.y -= 98/1.5
                    for i in range(len(objetinventairerect)):
                        objetinventairerect[i][1] +=98
            if event.type==MOUSEMOTION:
                testrect.x=event.pos[0]
                testrect.y=event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if testmask.overlap(curseurmask,(curseurrect.x-testrect.x, curseurrect.y-testrect.y)):
                    follow=True
                if event.button==2:
                    if 287<=testrect.x<360:
                        for i in range (len (objetinventairerect)):
                            if testrect.colliderect(objetinventairerect[i]) and inventaire[i][1]>0:

                                inventairefi = open("save1/inventaire", "r")
                                inventairestr = inventairefi.read().split(",")
                                inventairefi.close()
                                if inventairestr[i] in consommable:
                                    inventaire[i][1] -= 1
                                    fi=open("save1/objet/"+inventairestr[i], "w")
                                    fi.write(str(inventaire[i][1]))
                                    fi.close()
                                    objetinventaireimage[i]=pygame.image.load("inventory/objetinventaire.png").convert_alpha()
                if event.button==5:
                    if 287<=testrect.x and 160<=testrect.y and curseurrect.y<558:
                        curseurrect.y += (99/1.5)
                        for i in range (len(objetinventairerect)):
                            objetinventairerect[i][1]-=98
                if event.button == 4 :
                    if 287 <= testrect.x and 160<=testrect.y and  objetinventairerect[0][1]<160:
                        curseurrect.y -= (98/1.5)
                        for i in range(len(objetinventairerect)):
                            objetinventairerect[i][1] +=98

            if event.type == MOUSEBUTTONUP:
                follow=False




        fenetre.blit(fond,(0,0))
        fenetre.blit(emplacementperso0, (0,70))
        emplacementperso0.blit(perso0, (75,75))
        fenetre.blit(bandeauhaut, (0,0))
        fenetre.blit(interfaceinvent,(288,70))
        fenetre.blit(stuff_actuel,(0,263))
        for i in range (10):
            if objetinventairerect[i][1]>=150:
                fenetre.blit(objetinventaireimage[i], objetinventairerect[i])
        if follow==True:
            if 558>=curseurrect.y>=145:
                savecurseur=curseurrect.y
                curseurrect.y=testrect.y
            if 558>curseurrect.y>145:
                for i in range (len(objetinventairerect)):
                    objetinventairerect[i][1] += 1.5*(savecurseur-curseurrect.y)
        if curseurrect.y<=145:
            for i in range (len(objetinventairerect)):
                objetinventairerect[i][1]=160+99*i
        if curseurrect.y>558:
            curseurrect.y=558
        if curseurrect.y<145:
            curseurrect.y=145
        if queteactive!="":
           bandeauhaut.blit(police.render(queteactive + " : "+ mission, False, (53,255,251)), (10,10))
        for i in range (len(inventaire)):
            objetinventaireimage[i].blit(inventaire[i][0], (10,8))
            objetinventaireimage[i].blit(police.render("Quantitée : "+str(inventaire[i][1]), False, (40, 191, 188)), (95, 10))
        for i in range (len(lior)):
            bandeauhaut.blit(listechiffre[int(lior[i])], (720-22*i, 5))

        fenetre.blit(curseur, curseurrect)
        clock.tick(60)
        pygame.display.flip()

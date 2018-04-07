import pygame
from pygame.locals import*
from sys import exit
from imageinterfacetoload import *
def printinvent(fenetre):
    clock = pygame.time.Clock()
    fond = pygame.image.load("inventory\\fond.jpg").convert()
    follow = False
    curseurrect.x=769
    curseurrect.y=145
    objetinventairerect = []
    quetefi = open("quetes\\active", "r")
    queteactive=quetefi.read()
    queteactive =queteactive.capitalize()
    quetefi.close()
    if queteactive != "":
        missionfi=open("quetes\\"+queteactive+"\\toprint")
        mission=missionfi.read()
        missionfi.close()
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

            if event.type == MOUSEBUTTONDOWN:
                if testmask.overlap(curseurmask,(curseurrect.x-testrect.x, curseurrect.x-testrect.x)):
                    follow=True
            if event.type == MOUSEBUTTONUP:
                follow=False
            if event.type==MOUSEMOTION:
                testrect.x=event.pos[0]
                testrect.y=event.pos[1]



        fenetre.blit(fond,(0,0))
        fenetre.blit(emplacementperso0, (0,70))
        emplacementperso0.blit(perso0, (75,75))
        fenetre.blit(bandeauhaut, (0,0))
        fenetre.blit(interfaceinvent,(288,70))
        fenetre.blit(stuff_actuel,(0,263))
        for i in range (10):
            objetinventairerect.append([287, 160+99*i])
            if objetinventairerect[i][1]>=150:
                fenetre.blit(objetinventaire, objetinventairerect[i])
        if follow==True:
            if 558>=curseurrect.y>=145:
                savecurseur=curseurrect.y
                curseurrect.y=testrect.y
            if 558>curseurrect.y>145:
                for i in range (len(objetinventairerect)):
                    objetinventairerect[i][1]+=1.5*(savecurseur-curseurrect.y)
        if curseurrect.y>558:
            curseurrect.y=558
        if curseurrect.y<145:
            curseurrect.y=145
        if queteactive!="":
           bandeauhaut.blit(police.render(queteactive + " : "+ mission, False, (53,255,251)), (10,10))

        fenetre.blit(curseur, curseurrect)
        clock.tick()
        pygame.display.flip()

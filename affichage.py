import pygame
from pygame.locals import*
from random import *
from fennemi import *
import time
from classes_tpt import*

def affichage(action,tour,choix):
    
    my_font = pygame.font.SysFont("Calibri", 18)#les different taille d'ecriture
    my_font2 = pygame.font.SysFont("Calibri", 21)
    fond=pygame.image.load("fon\\fon.png")
    bandeaubleue = pygame.image.load("animation\\Fightblue.png").convert_alpha()
    bandeaurouge = pygame.image.load("animation\\Fightred.png").convert_alpha()

    position1=(610,180)#la position du perso qui jou
    position2=(625,100)#la position du perso qui attent
    position3=(640,20)#la position du perso qui attent
    positionpv1=(760,180)#la position des pv du perso qui jou
    positionpv2=(760,100)#la position des pv du perso qui attend
    positionpv3=(760,20 )#la position des pv du perso qui attend
    position_ennemi1=(100,100)  
    
    fenetre.blit(fond,(0,0))
    for i in range(4):
        fenetre.blit(my_font.render(action[i], False, (255,255,255)),(530,500+i*20))

    fenetre.blit(my_font2.render(str(enemitipe.vie), False, (255,255,255)),(40,60))
    if tour==1:
        fenetre.blit(my_font.render(str(perso_joueur.mana), False, (255,255,255)),(80,500))
        fenetre.blit(my_font.render(str(perso_joueur.fleche), False, (255,255,255)),(80,520))
        fenetre.blit(my_font.render("mana:", False, (255,255,255)),(20,500))
        fenetre.blit(my_font.render("fleches:", False, (255,255,255)),(20,520))
    if objet.menu_==1:
        fenetre.blit(my_font.render(str(soin.quantite), False, (255,255,255)),(670,520))
        fenetre.blit(my_font.render(str(resurection.quantite), False, (255,255,255)),(670,500))
    if tour==1:
        if sinatra.active==False:
            david.rect=position2 #endroit de spawn du perso
            perso_joueur.rect=position1
        else:
            sinatra.rect=position3
            david.rect=position2 #endroit de spawn du perso
            perso_joueur.rect=position1
        if sinatra.active==True:
            fenetre.blit(sinatra.image,sinatra.rect)
        fenetre.blit(david.image,david.rect)
        fenetre.blit(perso_joueur.image,perso_joueur.rect)

        fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255,255,255)),positionpv1)
        fenetre.blit(my_font2.render(str(david.vie), False, (255,255,255)),positionpv2)
        if sinatra.active==True:
            fenetre.blit(my_font2.render(str(sinatra.vie), False, (255,255,255)),positionpv3)

    if tour==2:
        if sinatra.active==False:
            david.rect=position1 #endroit de spawn du perso
            perso_joueur.rect=position2
        else:
            sinatra.rect=position2
            david.rect=position1 #endroit de spawn du perso
            perso_joueur.rect=position3
        fenetre.blit(perso_joueur.image,perso_joueur.rect)
        if sinatra.active==True:
            fenetre.blit(sinatra.image,sinatra.rect)
        fenetre.blit(david.image,david.rect)
        fenetre.blit(my_font2.render(str(david.vie), False, (255,255,255)),positionpv1)
        if sinatra.active==True:
            fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255,255,255)),positionpv3)
            fenetre.blit(my_font2.render(str(sinatra.vie), False, (255,255,255)),positionpv2)
        else:
            fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255,255,255)),positionpv2)
    if tour==3:
        david.rect=position3 #endroit de spawn du perso
        perso_joueur.rect=position2
        sinatra.rect=position1
        fenetre.blit(david.image,david.rect)
        fenetre.blit(perso_joueur.image,perso_joueur.rect)
        fenetre.blit(sinatra.image,sinatra.rect)
        fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255,255,255)),positionpv2)
        fenetre.blit(my_font2.render(str(sinatra.vie), False, (255,255,255)),positionpv1)
        fenetre.blit(my_font2.render(str(david.vie), False, (255,255,255)),positionpv3)



    fenetre.blit(enemitipe.image,position_ennemi1)
    if choix==1:
        fenetre.blit(my_font.render("-", False, (255,255,255)),(520,500))
    elif choix==2:
        fenetre.blit(my_font.render("-", False, (255,255,255)),(520,520))
    elif choix==3:
        fenetre.blit(my_font.render("-", False, (255,255,255)),(520,540))
    elif choix==4:
        fenetre.blit(my_font.render("-", False, (255,255,255)),(520,560))
    pygame.display.flip()    


def affichageanim(d,tour,variableanim):
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont("Calibri", 36)
    fond = pygame.image.load("fon\\fon.png")
    bandeaubleue = pygame.image.load("animation\\Fightblue.png").convert_alpha()
    bandeaurouge = pygame.image.load("animation\\Fightred.png").convert_alpha()
    fouldebeu = pygame.image.load("animation\\fireball.png").convert_alpha()
    fouldebeunul = pygame.image.load("animation\\fireballkitomb.png").convert_alpha()

    position = (610, 180)  # la position du perso qui jou
    position_ennemi1 = (100, 100)
    i=0
    fenetre.blit(fond, (0, 0))
    while i<42:
        for event in pygame.event.get():
            if event.type == QUIT :# pour pouvoir quitter le jeux
                pygame.quit()
                exit()
        fenetre.blit(bandeaubleue,(810-i*10,200))
        fenetre.blit(bandeaurouge,(-410+i*10,200))
        i+=1
        clock.tick(60)
        pygame.display.flip()
        
    i=0
    while i<160:
        fenetre.blit(fond, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT :# pour pouvoir quitter le jeux
                pygame.quit()
                exit()
        fenetre.blit(bandeaubleue, (389, 200))
        fenetre.blit(bandeaurouge, (11, 200))
        if variableanim==1:
            if tour==1:
                fenetre.blit(perso_joueur.image, (689,200))
            if tour==2:
                fenetre.blit(david.image, (689,200))
            if tour==3:
                fenetre.blit(sinatra.image, (689,200))
            fenetre.blit(enemitipe.image, (11,200))
            if i < 80:
                fenetre.blit(fouldebeu, (689-i*6, 250))
            else:
                fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))
        if variableanim == 2:
            fenetre.blit(perso_joueur.image, (689,200))
            fenetre.blit(enemitipe.image, (11,200))
            if i < 20:
                fenetre.blit(fouldebeu, (689-i*6, 250))
            else:
                fenetre.blit(fouldebeunul, (569, 250+i*2))

        else:
            if i<80:
                if tour==1:
                    fenetre.blit(perso_joueur.image, (689-i*4,200))
                if tour==2:
                    fenetre.blit(david.image, (689-i*4,200))
                if tour==3:
                    fenetre.blit(sinatra.image, (689-i*4,200))
            if i>80:
                if tour==1:
                    fenetre.blit(perso_joueur.image2, (289,200))
                if tour==2:
                    fenetre.blit(david.image2, (289,200))
                if tour==3:
                    fenetre.blit(sinatra.image2, (289,200))
                fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41,180))
        fenetre.blit(enemitipe.image, (11,200))

        clock.tick(60)
        pygame.display.flip()
        i+=1



def affichageanimennemi(d,tour):
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont("Calibri", 36)
    fond = pygame.image.load("fon\\fon.png")
    bandeaubleue = pygame.image.load("animation\\Fightblue.png").convert_alpha()
    bandeaurouge = pygame.image.load("animation\\Fightred.png").convert_alpha()
    position = (610, 180) 
    position_ennemi1 = (100, 100)
    i=0
    fenetre.blit(fond, (0, 0))
    while i<42:
        for event in pygame.event.get():
            if event.type == QUIT :# pour pouvoir quitter le jeux
                pygame.quit()
                exit()
        fenetre.blit(bandeaubleue,(810-i*10,200))
        fenetre.blit(bandeaurouge,(-410+i*10,200))
        i+=1
        clock.tick(60)
        pygame.display.flip()
    i=0
    while i < 160:
        for event in pygame.event.get():
            if event.type == QUIT :# pour pouvoir quitter le jeux
                pygame.quit()
                exit()
        fenetre.blit(bandeaubleue, (389, 200))
        fenetre.blit(bandeaurouge, (11, 200))
        if i < 80:
            if tour == 1:
                fenetre.blit(perso_joueur.image, (659, 200))
            if tour == 2:
                fenetre.blit(david.image, (659, 200))
            if tour == 3:
                fenetre.blit(sinatra.image, (659, 200))
            fenetre.blit(enemitipe.image, (11 + i*4, 200))
        if i > 80:
            fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
            fenetre.blit(enemitipe.image, (411, 200))
            if tour == 1:
                fenetre.blit(perso_joueur.image, (659, 200))
            if tour == 2:
                fenetre.blit(david.image, (689, 200))
            if tour == 3:
                fenetre.blit(sinatra.image, (659, 200))
        i += 1
        clock.tick(60)
        pygame.display.flip()

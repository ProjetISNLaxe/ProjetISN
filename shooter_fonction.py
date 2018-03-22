 #!/usr/bin/env python
#-*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from random import *
from math import cos
from classes import*
from pygame import*
from constantes import*

def surchauffer(surchauffe, surchauffed, fenetre):
        surchauffe-=1         #On fais baisser al surchauffe
        position_surchauffe=685
        if surchauffe>100:
            fenetre.blit(surchauffed,(position_surchauffe,560))      #On blit le carée de surchauffe
        if surchauffe>200:
            fenetre.blit(surchauffed,(position_surchauffe,525))
        if surchauffe>300:
            fenetre.blit(surchauffed,(position_surchauffe,490))
        if surchauffe>400:
            fenetre.blit(surchauffed,(position_surchauffe,455))
        if surchauffe>500:
            fenetre.blit(surchauffed,(position_surchauffe,420))
        if surchauffe>600:
            fenetre.blit(surchauffed,(position_surchauffe,385))
        if surchauffe>700:
            fenetre.blit(surchauffed,(position_surchauffe,350))
        if surchauffe>800:
            fenetre.blit(surchauffed,(position_surchauffe,315))
        if surchauffe>900:
            fenetre.blit(surchauffed,(position_surchauffe,280))
        return surchauffe

def verification_score(score, vie, vitesseennemiy):
        if score%20 == 0 and score!=0:       #Tous les 20 ennemis mort on augmente la vitesse de 10%
              vitesseennemiy=vitesseennemiy*1.10
        if score%10 == 0 and score!=0:
              vie+=1
        return vie, vitesseennemiy

def shooter(fenetre, glitch):

     pygame.key.set_repeat(200,15)           #refrappe
     clock = pygame.time.Clock()             #horloge interne


     groupesprite=pygame.sprite.Group()
     fenetre_taille=fenetre.get_size()
     fond=imfond(fenetre_taille)                            #charge l'image de fond

     perso=personnage(fenetre_taille, glitch)

     tirennemi=pygame.image.load("ennemi\\tir_ennemi.png").convert_alpha()              #charge les images des tirs
     tir=pygame.image.load("perso\\bullet_n-ship.png").convert_alpha()
     tir_mask=pygame.mask.from_surface(tir)
     tirennemi_mask=pygame.mask.from_surface(tirennemi)

     p=0

     ennemi_1=ennemi1(fenetre_taille)
     ennemi_2=ennemi2(fenetre_taille)
     groupesprite.add(ennemi_1,ennemi_2, perso)

     miniboss=clminiboss(fenetre_taille)

     bulle=pygame.image.load("perso\\N-Ship_shield.png").convert_alpha()

     coeur=pygame.image.load("HUD\\heart(1).png").convert_alpha()                    #charge l'image coeur)
        

     surchauffed=pygame.image.load("HUD\\overheat.png").convert_alpha()


     myfont=pygame.font.SysFont("monospace", 20)

     increment=0

     vitessex= 5     #Vitesse  vaisseau x
     vitessey = 2.5     #Vitesse  vaisseau y

     surchauffe=0     #Surchauffe
     surchauffemax=1000

     h=0          #Variable pour la  de l'

     ex=False     # qui  si on doit animer l'explosion
     p=0          #nombre de boucle pour explosion

     pause=True     #pause

     score=SCORE_BASE     # Nombre d'ennemis mort


     while 1 : # les deplacements
      while perso.vie != -1:
        for event in pygame.event.get():
            if event.type == QUIT : # quitter le jeux en cliquant sur la croix
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE: # Echap pour quitter
                    pygame.quit()
                    exit()
                # les deplacements

                if event.key==PAUSE:  #Si on met en Pause
                    pause=True
                    while pause:
                        pygame.time.delay(1000)  #Delai pour ne pas qu'il  l'appuie de la touche
                        for event in pygame.event.get():
                           if event.type == QUIT:  #Pour pouvoir tout de  quitter
                              pygame.quit()
                              exit()
                           if event.type==KEYDOWN:
                               if event.key==K_ESCAPE:
                                  perso.vie=0
                               if event.key==K_p: #On  a la pause si on appuie sur p
                                       pause=False

        perso.eventkey()
        ennemi_1.move(score)
        ennemi_2.move(score)
        ennemi_2.shoot(increment)
        miniboss.attaque2(score, increment)
        miniboss.attaque4(score, increment)
        miniboss.attaque5(score, increment)
        fond.deplacement()
        ennemi_1.collision(perso)
        ennemi_2.collision(perso)
        ennemi_1.explosionanim()
        ennemi_2.explosionanim()
        miniboss.attaque6(score, increment, perso)
        for k in range(perso.nbrTir):
            if ennemi_1.mask.overlap(tir_mask, (perso.tirx[k]-ennemi_1.rect.x, perso.tiry[k]-ennemi_1.rect.y)) and perso.tiry[k]>10 and ennemi_1.alive:# colision entre projectille et ennemi.
               ennemi_1.inexplosion=True
               ennemi_1.explosion_rect=Rect(ennemi_1.rect.x-25, ennemi_1.rect.y-25, 192,192)
                               #On anime l'explosion
               d = randrange(40,500)      #On fais  l'ennemi a une  sur x
               ennemi_1.rect=Rect(d,-ennemi_1.rect.y-200,64,100)
               perso.tirx[k]=-555                 #On fais disparaitre le tir
               score+=1                   #On  le score

        for b in range(perso.nbrTir):
            if ennemi_2.mask.overlap(tir_mask, (perso.tirx[b]-ennemi_2.rect.x, perso.tiry[b]-ennemi_2.rect.y)) and perso.tiry[b]>10 and ennemi_2.alive:# colision entre projectille et ennemi.
               ennemi_2.inexplosion=True             #On anime l'explosion
               ennemi_2.explosion_rect=Rect(ennemi_2.rect.x-25, ennemi_2.rect.y-25, 192,192)
               o = randrange(40,500)      #On fais spawner l'ennemi a une coordonee sur x
               ennemi_2.rect=Rect(o,-100,64,130)
               perso.tirx[b]=-555                 #On fais disparaitre le tir
               score+=1                   #On incremente le score

        if ennemi_1.incollision and score < SCORE_MINIBOSS:#Collision ennemi perso
               perso.inexplosion=True
               perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
               ennemi_1.inexplosion=True
               ennemi_1.explosion_rect=Rect(ennemi_1.rect.x-25, ennemi_1.rect.y-25, 192,192)
                      #On anime l'explosion
               if perso.immortel==False:
                    perso.vie-=1                #On perd une vie si on est pas immortel
                    perso.immortel=True
               ennemi_1.respawn()
               score+=1                   #On  le score
               ennemi_1.incollision=False

        if ennemi_2.incollision and score < SCORE_MINIBOSS and score >= SCORE_ENNEMI_2:#Collision ennemi perso
               perso.inexplosion=True
               perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
               ennemi_2.inexplosion=True                #On anime l'explosion
               ennemi_2.explosion_rect=Rect(ennemi_2.rect.x-25, ennemi_2.rect.y-25, 192,192)
               if perso.immortel==False:
                    perso.vie-=1                #On perd une vie si on est pas immortel
                    perso.immortel=True
               ennemi_2.respawn()
               score+=1                   #On  le score
               ennemi_2.incollision=False

        for q in range(ennemi_2.nbrTir):
            if perso.mask.overlap(tirennemi_mask,(ennemi_2.tirx[q]-perso.rect.x,ennemi_2.tiry[q]-perso.rect.y)):# colision entre projectille et perso
               ennemi_2.tirx[q]=-555           #On fait disparaitre le tir
               perso.inexplosion=True
               perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
               if perso.immortel==False:

                     perso.vie-=1               #On perd une vie si on est pas immortel
                     perso.immortel=True

        if pygame.sprite.collide_mask(ennemi_1,ennemi_2) and score >= SCORE_ENNEMI_2 and score <SCORE_MINIBOSS and ennemi_1.rect.y>0: # colision entre ennemi 1 et 2 (que si l'ennemi 2 existe)
               ennemi_1.inexplosion=True
               ennemi_1.explosion_rect=Rect(ennemi_1.rect.x-25, ennemi_1.rect.y-25, 192,192)
               ennemi_1.respawn()
               ennemi_2.respawn()
               score+=1                   #On incremente le score



        for n in range (perso.nbrTir):
           if miniboss.maskcanon.overlap(tir_mask, (perso.tirx[n]-miniboss.rectcanon[0], perso.tiry[n]-miniboss.rectcanon[1])) and score >=SCORE_MINIBOSS and miniboss.canonalive==True:
               if miniboss.canonPtVie>0:
                     miniboss.canonPtVie-=1
                     perso.tirx[n]=10000
                     score+=1
               elif miniboss.canonPtVie==0:
                     miniboss.canonalive=False
                     perso.tirx[n]=10000
        for w in range (perso.nbrTir):
           if miniboss.maskcanoncasse.overlap(tir_mask, (perso.tirx[w]-miniboss.rectcanon[0], perso.tiry[w]-miniboss.rectcanon[1])) and score >=SCORE_MINIBOSS and miniboss.canonalive==False:
               perso.tirx[w]=10000
        for g in range (perso.nbrTir):
           if miniboss.mask.overlap(tir_mask, (perso.tirx[g]-miniboss.rect.x, perso.tiry[g]-miniboss.rect.y)) and score >=SCORE_MINIBOSS and miniboss.alive==True:
               if miniboss.canonalive==False:
                    if miniboss.ptVie>0:
                          perso.tirx[g]=10000
                          miniboss.perdvie()
                    else:
                          perso.tirx[g]=10000
               else:
                    perso.tirx[g]=10000


        for y in range (perso.nbrTir):
            if miniboss.eclairmask.overlap(tir_mask, (perso.tirx[y]-miniboss.eclairrect.x, perso.tiry[y]-miniboss.eclairrect.y)) and miniboss.unlimitedpoweer==True and miniboss.canonalive==True:
               perso.tirx[y]=10000
        for q in range(miniboss.nbrTir):
            if perso.mask.overlap(tirennemi_mask,(miniboss.tirx[q]-perso.rect.x,miniboss.tiry[q]-perso.rect.y)):# colision entre projectille et perso
               miniboss.tirx[q]=-555           #On fait disparaitre le tir
               perso.inexplosion=True
               perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
               if perso.immortel==False:

                     perso.vie-=1               #On perd une vie si on est pas immortel
                     perso.immortel=True

        if perso.mask.overlap(miniboss.boulemask,(miniboss.boulerect.x-perso.rect.x,miniboss.boulerect.y-perso.rect.y)) and miniboss.energiebowl==True and miniboss.canonalive==True:# colision entre bouleminiboss et perso
            miniboss.bouleattak=False
            miniboss.energiebowl=False
            miniboss.boulerect.y=110
            miniboss.boulerect.x=250
            miniboss.test3=True
            miniboss.increment_boule=0
            perso.inexplosion=True
            perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
            if perso.immortel==False:

                 perso.vie-=1               #On perd une vie si on est pas immortel
                 perso.immortel=True
        if perso.mask.overlap(miniboss.boulemask1,(miniboss.boulerect1.x-perso.rect.x,miniboss.boulerect1.y-perso.rect.y)) and miniboss.energiebowl1==True and miniboss.canonalive==True:# colision boule miniboss perso
            miniboss.bouleattak1=False
            miniboss.energiebowl1=False
            miniboss.boulerect1.y=110
            miniboss.boulerect1.x=515
            miniboss.test4=True
            miniboss.increment_boule1=0
            perso.inexplosion=True
            perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
            if perso.immortel==False:

                 perso.vie-=1               #On perd une vie si on est pas immortel
                 perso.immortel=True
        if perso.mask.overlap(miniboss.boulemask2,(miniboss.boulerect2.x-perso.rect.x,miniboss.boulerect2.y-perso.rect.y)) and miniboss.laser==True and miniboss.canonalive==False:# colision boule miniboss perso
            perso.inexplosion=True
            perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
            if perso.immortel==False:
                 perso.vie-=1               #On perd une vie si on est pas immortel
                 perso.immortel=True
        if perso.mask.overlap(miniboss.lasermask,(miniboss.laserrect.x-perso.rect.x,miniboss.laserrect.y-perso.rect.y)) and miniboss.laseer==True and miniboss.canonalive==False:# colision boule miniboss perso  
            print("yess")
            if perso.immortel==False:
                 perso.inexplosion=True
                 perso.explosion_rect=Rect(perso.rect.x-25, perso.rect.y-25, 192,192)
                 perso.vie-=1               #On perd une vie si on est pas immortel
                 perso.immortel=True
        ennemi_1.explosionanim()
        ennemi_2.explosionanim()

        perso.explosionanim()
        if fond.deplacement1==True:
             fenetre.blit(fond.image1, fond.rect1) #On fais apparaitre le fond
        if fond.deplacement2==True:
             fenetre.blit(fond.image2, fond.rect2)
        if perso.vie>0:   
             fenetre.blit(perso.image,perso.rect)
        if perso.immortel==True and perso.vie>0:
            position_bulle=Rect(perso.rect.x-12.5, perso.rect.y-12.5,125,125)
            fenetre.blit(bulle, position_bulle)
            h+=1
            if h>280:
                perso.immortel=False
                h=0
        if perso.vie==0:
                perso.death()
                fenetre.blit(self.persodeath[0],self.persodeathrect[0])
                fenetre.blit(self.persodeath[1],self.persodeathrect[1])
                fenetre.blit(self.persodeath[2],self.persodeathrect[2])
        miniboss.attaque1(score)
        miniboss.attaque3(score)

        if perso.rect.x<=400+perso.size[0]/2:
            miniboss.persoinzone=True
            miniboss.persoinzone1=False
        elif perso.rect.x>=400+perso.size[0]/2:
            miniboss.persoinzone=False
            miniboss.persoinzone1=True

        if miniboss.laseer==True:
            fenetre.blit(miniboss.laserimage, (miniboss.boulerect2[0]-4,miniboss.boulerect2[1]+10))
        if miniboss.laser==True and miniboss.attaque1_moveinvert==False and miniboss.attaque1_movevert==False:
            fenetre.blit(miniboss.bouleimage2, miniboss.boulerect2)

        if score>=SCORE_MINIBOSS and miniboss.alive==True:
            fenetre.blit(miniboss.image, miniboss.rect)


        if score>=SCORE_MINIBOSS:
          if miniboss.canonalive==True:
            fenetre.blit(miniboss.imgcanon, miniboss.rectcanon)
          else:
            fenetre.blit(miniboss.imgcanoncasse, miniboss.rectcanon)


        
        if ennemi_2.nbrTir>0 and ennemi_2.tir_ok==True and score<SCORE_MINIBOSS:  #On affiche tous les tirs ennemis si ils existent
            for i in range(ennemi_2.nbrTir):
                ennemi_2.tiry[i]+=6
                fenetre.blit(tirennemi,(ennemi_2.tirx[i],ennemi_2.tiry[i]))

        if perso.nbrTir>0:#on affiche tout les tir
            for i in range(perso.nbrTir):
                perso.tiry[i]-=6
                fenetre.blit(tir,(perso.tirx[i],perso.tiry[i]))

        if score>=0 and score <SCORE_MINIBOSS:
            ennemi_1.alive=True
            fenetre.blit(ennemi_1.image,ennemi_1.rect)

        if score>=SCORE_ENNEMI_2 and score<SCORE_MINIBOSS:                     #On affiche l'ennemi 2 que si on a 10 en score
            ennemi_2.alive=True
            fenetre.blit(ennemi_2.image, ennemi_2.rect)
        elif score>=SCORE_MINIBOSS:
            ennemi_2.alive=False
            ennemi_1.alive=False


        for z in range(miniboss.nbrTir):
                miniboss.tiry[z]+=10
                fenetre.blit(tirennemi,(miniboss.tirx[z],miniboss.tiry[z]))

        if miniboss.unlimitedpoweer==True and miniboss.canonalive==True:
            fenetre.blit(miniboss.eclairimage, miniboss.eclairrect)



        if ennemi_1.explosionact==True:
            fenetre.blit(ennemi_1.explosion, ennemi_1.explosion_rect)

        if ennemi_2.explosionact==True:
            fenetre.blit(ennemi_2.explosion, ennemi_2.explosion_rect)

        if perso.explosionact==True:
            fenetre.blit(perso.explosion, perso.explosion_rect)

         
        

        

        if miniboss.energiebowl==True and miniboss.canonalive==True:
            miniboss.boulemovex=(perso.rect.x+perso.size[0]/2-250)/75
            miniboss.boulemovey=(110+perso.rect.y)/75
            fenetre.blit(miniboss.bouleimage, miniboss.boulerect)
        if miniboss.energiebowl1==True and miniboss.canonalive==True:
            miniboss.boulemove1x=(perso.rect.x+perso.size[0]/2-515)/75
            miniboss.boulemove1y=(110+perso.rect.y)/75
            fenetre.blit(miniboss.bouleimage1, miniboss.boulerect1)

        for k in range (perso.vie):  #On affiche les coeurs de vie
            fenetre.blit(coeur,(760-35*k, 10))


        if perso.surchauffe>0:       #On  si on surchauffe ou pas
            perso.surchauffe=surchauffer(perso.surchauffe, surchauffed, fenetre)

        increment+=1           #On augmente l'incremnent pour les tirs ennemis

        pygame.display.flip()  #On raffraichis l'ecran
        clock.tick(60)         #60 FPS
        
      
      pygame.display.flip()
      return

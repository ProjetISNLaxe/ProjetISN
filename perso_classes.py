import pygame
from pygame.locals import *


class Personnage(pygame.sprite.Sprite):

    def __init__(self):

        self.B1 = pygame.image.load("perso/B1.png")
        self.B2 = pygame.image.load("perso/B2.png")
        self.B3 = pygame.image.load("perso/B3.png")

        self.F1 = pygame.image.load("perso/F1.png")
        self.F2 = pygame.image.load("perso/F2.png")
        self.F3 = pygame.image.load("perso/F3.png")

        self.R1 = pygame.image.load("perso/R1.png")
        self.R2 = pygame.image.load("perso/R2.png")
        self.R3 = pygame.image.load("perso/R3.png")

        self.L1 = pygame.image.load("perso/L1.png")
        self.L2 = pygame.image.load("perso/L2.png")
        self.L3 = pygame.image.load("perso/L3.png")

        self.imageperso = self.B1

        self.size = self.imageperso.get_size()
        self.rect = self.imageperso.get_rect()
        self.rect.x=400-self.size[0]+16
        self.rect.y= 600-self.size[0]
        self.mask = pygame.mask.from_surface(self.imageperso)
        self.inc = 0
        self.moveD=False
        self.moveR=False
        self.moveT=False
        self.moveL=False
        self.allowedT=True
        self.allowedR = True
        self.allowedL = True
        self.allowedD = True

    def moveTop(self):
        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.B1
            self.rect.y -= self.size[1] / 3
        if self.inc==10:
            self.imageperso = self.B2
            self.rect.y -= self.size[1] / 3
        if self.inc==20:
            self.imageperso = self.B3
            self.rect.y -= self.size[1] / 3
        if self.inc == 30:
            self.inc = 0
            self.moveT=False

    def moveRight(self):
        self.inc += 1
        if self.inc==1:
            self.imageperso = self.R1
            self.rect.x += self.size[0] / 3
        if self.inc==10:
            self.imageperso = self.R2
            self.rect.x += self.size[0] / 3
        if self.inc==20:
            self.imageperso = self.R3
            self.rect.x += self.size[0] / 3
        if self.inc == 30:
            self.inc = 0
            self.moveR= False

    def moveLeft(self):

        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.L1
            self.rect.x -= self.size[0] / 3
        if self.inc==10:
            self.imageperso = self.L2
            self.rect.x -= self.size[0] / 3
        if self.inc==20:
            self.imageperso = self.L3
            self.rect.x -= self.size[0] / 3
        if self.inc == 30:
            self.inc = 0
            self.moveL=False

    def moveDown(self):
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.F1
            self.rect.y += self.size[1] / 3
        if self.inc==10:
            self.imageperso = self.F2
            self.rect.y += self.size[1] / 3
        if self.inc==20:
            self.imageperso = self.F3
            self.rect.y += self.size[1] / 3
        if self.inc == 30:
            self.inc = 0
            self.moveD=False

    def eventkey(self):
        tkey = pygame.key.get_pressed()
        if tkey[K_UP] and self.allowedT==True:
            self.moveT=True
        if tkey[K_DOWN] and self.allowedD==True:
            self.moveD=True
        if tkey[K_LEFT] and self.allowedL==True:
            self.moveL=True
        if tkey[K_RIGHT] and self.allowedR==True:
            self.moveR=True
        if self.moveT==True:
            self.moveTop()
        if self.moveR==True:
            self.moveRight()
        if self.moveL==True:
            self.moveLeft()
        if self.moveD==True:
            self.moveDown()

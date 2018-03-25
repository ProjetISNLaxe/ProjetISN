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
        self.moveDmap = False
        self.moveRmap = False
        self.moveTmap = False
        self.moveLmap = False
        self.allowedT=True
        self.allowedR = True
        self.allowedL = True
        self.allowedD = True
        self.allowedTmap = True
        self.allowedRmap = True
        self.allowedLmap = True
        self.allowedDmap = True

    def moveTop(self):
        self.allowedR = False
        self.allowedL = False
        self.allowedD = False
        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.B1
            self.rect.y -= self.size[1] / 6
        if self.inc==5:
            self.imageperso = self.B2
            self.rect.y -= self.size[1] / 6
        if self.inc==10:
            self.imageperso = self.B3
            self.rect.y -= self.size[1] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveT=False
            self.allowedR = True
            self.allowedL = True
            self.allowedD = True

    def moveRight(self):
        self.allowedT = False
        self.allowedL = False
        self.allowedD = False
        self.inc += 1
        if self.inc==1:
            self.imageperso = self.R1
            self.rect.x += self.size[0] / 6
        if self.inc==5:
            self.imageperso = self.R2
            self.rect.x += self.size[0] / 6
        if self.inc==10:
            self.imageperso = self.R3
            self.rect.x += self.size[0] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveR= False
            self.allowedT = True
            self.allowedL = True
            self.allowedD = True

    def moveLeft(self):
        self.allowedT = False
        self.allowedR = False
        self.allowedD = False
        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.L1
            self.rect.x -= self.size[0] / 6
        if self.inc==5:
            self.imageperso = self.L2
            self.rect.x -= self.size[0] / 6
        if self.inc==10:
            self.imageperso = self.L3
            self.rect.x -= self.size[0] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveL=False
            self.allowedT = True
            self.allowedR = True
            self.allowedD = True

    def moveDown(self):
        self.allowedT = False
        self.allowedR = False
        self.allowedL = False
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.F1
            self.rect.y += self.size[1] / 6
        if self.inc==5:
            self.imageperso = self.F2
            self.rect.y += self.size[1] / 6
        if self.inc==10:
            self.imageperso = self.F3
            self.rect.y += self.size[1] / 6
        if self.inc ==15:
            self.inc = 0
            self.moveD=False
            self.allowedT = True
            self.allowedR = True
            self.allowedL = True

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

    def mapDown(self, position):
        self.allowedRmap = False
        self.allowedLmap = False
        self.allowedTmap = False
        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.F1
            position.y -= self.size[1] / 6
        if self.inc==5:
            self.imageperso = self.F2
            position.y -= self.size[1] / 6
        if self.inc==10:
            self.imageperso = self.F3
            position.y -= self.size[1] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveDmap=False
            self.allowedRmap = True
            self.allowedLmap = True
            self.allowedTmap = True

    def mapLeft(self, position):
        self.allowedTmap = False
        self.allowedRmap = False
        self.allowedDmap = False
        self.inc += 1
        if self.inc==1:
            self.imageperso = self.L1
            position.x += self.size[0] / 6
        if self.inc==5:
            self.imageperso = self.L2
            position.x += self.size[0] / 6
        if self.inc==10:
            self.imageperso = self.L3
            position.x += self.size[0] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveLmap= False
            self.allowedTmap = True
            self.allowedRmap = True
            self.allowedDmap = True

    def mapRight(self, position):
        self.allowedTmap = False
        self.allowedLmap = False
        self.allowedDmap = False
        self.inc += 1
        if self.inc ==1:
            self.imageperso = self.R1
            position.x -= self.size[0] / 6
        if self.inc==5:
            self.imageperso = self.R2
            position.x -= self.size[0] / 6
        if self.inc==10:
            self.imageperso = self.R3
            position.x -= self.size[0] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveRmap=False
            self.allowedTmap = True
            self.allowedLmap = True
            self.allowedDmap = True

    def mapTop(self, position):
        self.allowedDmap = False
        self.allowedRmap = False
        self.allowedLmap = False
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.B1
            position.y += self.size[1] / 6
        if self.inc == 5:
            self.imageperso = self.B2
            position.y += self.size[1] / 6
        if self.inc == 10:
            self.imageperso = self.B3
            position.y += self.size[1] / 6
        if self.inc == 15:
            self.inc = 0
            self.moveTmap = False
            self.allowedTDmap = True
            self.allowedRmap = True
            self.allowedLmap = True

    def mapkey(self, position):
        tkey = pygame.key.get_pressed()
        if tkey[K_UP] and self.allowedTmap == True:
            self.moveTmap = True
        if tkey[K_DOWN] and self.allowedDmap == True:
            self.moveDmap = True
        if tkey[K_LEFT] and self.allowedLmap == True:
            self.moveLmap = True
        if tkey[K_RIGHT] and self.allowedRmap == True:
            self.moveRmap = True
        if self.moveTmap == True:
            self.mapTop(position)
        if self.moveRmap == True:
            self.mapRight(position)
        if self.moveLmap == True:
            self.mapLeft(position)
        if self.moveDmap == True:
            self.mapDown(position)


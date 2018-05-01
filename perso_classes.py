import pygame
from pygame.locals import *
from random import *
from combatV3 import *
import random
import time


class Personnage(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.imageperso = self.B1
        self.size = self.imageperso.get_size()
        self.rect = self.imageperso.get_rect()
        self.rect = Rect(400 - self.size[0] + 16, 600 - self.size[1], self.size[0], self.size[1])
        self.mask = pygame.mask.from_surface(self.imageperso)
        goldf = open("save1\\invent\\cpic")
        self.gold = int(goldf.read())
        goldf.close()
        self.inc = 0
        self.moveD = False
        self.moveR = False
        self.moveT = False
        self.moveL = False
        self.moveDmap = False
        self.moveRmap = False
        self.moveTmap = False
        self.moveLmap = False
        self.allowedT = True
        self.allowedR = True
        self.allowedL = True
        self.allowedD = True
        self.allowedTmap = True
        self.allowedRmap = True
        self.allowedLmap = True
        self.allowedDmap = True

    def moveTop(self):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.B1
            self.rect.y -= int(self.size[1] / 4.5)
        if self.inc == 6:
            self.imageperso = self.B2
            self.rect.y -= int(self.size[1] / 4.5)
        if self.inc == 12:
            self.imageperso = self.B3
            self.rect.y -= int(self.size[1] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveT = False

    def moveRight(self):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.R1
            self.rect.x += int(self.size[0] / 4.5)
        if self.inc == 6:
            self.imageperso = self.R2
            self.rect.x += int(self.size[0] / 4.5)
        if self.inc == 12:
            self.imageperso = self.R3
            self.rect.x += int(self.size[0] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveR = False

    def moveLeft(self):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.L1
            self.rect.x -= int(self.size[0] / 4.5)
        if self.inc == 6:
            self.imageperso = self.L2
            self.rect.x -= int(self.size[0] / 4.5)
        if self.inc == 12:
            self.imageperso = self.L3
            self.rect.x -= int(self.size[0] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveL = False

    def moveDown(self):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.F1
            self.rect.y += int(self.size[1] / 4.5)
        if self.inc == 6:
            self.imageperso = self.F2
            self.rect.y += int(self.size[1] / 4.5)
        if self.inc == 12:
            self.imageperso = self.F3
            self.rect.y += int(self.size[1] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveD = False

    def mapDown(self, position):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.F1
            position.y -= int(self.size[1] / 4.5)
        if self.inc == 6:
            self.imageperso = self.F2
            position.y -= int(self.size[1] / 4.5)
        if self.inc == 12:
            self.imageperso = self.F3
            position.y -= int(self.size[1] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveDmap = False

    def mapLeft(self, position):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.L1
            position.x += int(self.size[0] / 4.5)
        if self.inc == 6:
            self.imageperso = self.L2
            position.x += int(self.size[0] / 4.5)
        if self.inc == 12:
            self.imageperso = self.L3
            position.x += int(self.size[0] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveLmap = False

    def mapRight(self, position):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.R1
            position.x -= int(self.size[0] / 4.5)
        if self.inc == 6:
            self.imageperso = self.R2
            position.x -= int(self.size[0] / 4.5)
        if self.inc == 12:
            self.imageperso = self.R3
            position.x -= int(self.size[0] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveRmap = False

    def mapTop(self, position):
        if random.random() <= 0.005:
            tourpartour()
        self.inc += 1
        if self.inc == 1:
            self.imageperso = self.B1
            position.y += int(self.size[1] / 4.5)
        if self.inc == 6:
            self.imageperso = self.B2
            position.y += int(self.size[1] / 4.5)
        if self.inc == 12:
            self.imageperso = self.B3
            position.y += int(self.size[1] / 4.5)
        if self.inc == 18:
            self.inc = 0
            self.moveTmap = False

    def eventkey(self, position, masque, taille):
        self.mask = pygame.mask.from_surface(self.imageperso)
        tkey = pygame.key.get_pressed()
        if tkey[K_UP] and position.y >= 0 or tkey[K_UP] and self.rect.y > 300:
            for i in range(int(self.size[1] * 2 / 3)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y - i - position.y)) or self.rect.x <= 0:
                    break
                if i == int(self.size[1] * 2 / 3 - 1):
                    self.moveTop()
        elif tkey[K_UP] and position.y <= 0:
            for i in range(int(self.size[1] * 2 / 3 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y - i)):
                    break
                if i == int(self.size[1] * 2 / 3):
                    self.mapTop(position)
        if tkey[K_DOWN] and position.y <= -taille[1] + 600 or tkey[K_DOWN] and self.rect.y < 200:

            for i in range(int(self.size[1] * 2 / 3 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - position.x, self.rect.y + 1 - position.y)) or self.rect.y >= 600 - \
                        self.size[1]:
                    break
                if i == int(self.size[1] * 2 / 3):
                    self.moveDown()
        elif tkey[K_DOWN] and position.y >= -taille[1] + 600:
            for i in range(int(self.size[1] * 2 / 3 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y + 1)):
                    break
                if i == int(self.size[1] * 2 / 3):
                    self.mapDown(position)

        if tkey[K_LEFT] and position.x >= 0 or tkey[K_LEFT] and self.rect.x > 400:
            for i in range(int(self.size[0] * 2 / 3 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x - i - position.x, self.rect.y - position.y)) or self.rect.x <= 0:
                    break
                if i == int(self.size[0] * 2 / 3):
                    self.moveLeft()
        elif tkey[K_LEFT] and position.x <= 0:
            for i in range(int(self.size[0] * 2 / 3 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x - i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] * 2 / 3):
                    self.mapLeft(position)

        if tkey[K_RIGHT] and position.x <= -taille[0] + 800 or tkey[K_RIGHT] and self.rect.x < 400:
            for i in range(int(self.size[0] * 2 / 3 + 1)):
                if masque.overlap(self.mask,
                                  (self.rect.x + i - position.x, self.rect.y - position.y)) or self.rect.x >= 800 - \
                        self.size[0]:
                    break
                if i == int(self.size[0] * 2 / 3):
                    self.moveRight()
        elif tkey[K_RIGHT] and position.x >= -taille[0] + 800:
            for i in range(int(self.size[0] * 2 / 3 + 1)):
                if masque.overlap(self.mask, (self.rect.x - position.x + i, self.rect.y - position.y)):
                    break
                if i == int(self.size[0] * 2 / 3):
                    self.mapRight(position)

        if masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)):
            try:
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        0] + position.x - self.rect.x) >= 0:
                    self.rect.x += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          0] + position.x - self.rect.x) <= 0:
                    self.rect.x -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            0] + position.x - self.rect.x) / 5
                if ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                        1] + position.y - self.rect.y) >= 0:
                    self.rect.y -= int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
                elif ((masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                          1] + position.y - self.rect.y) <= 0:
                    self.rect.y += int(
                        (masque.overlap(self.mask, (self.rect.x - position.x, self.rect.y - position.y)))[
                            1] + position.y - self.rect.y) / 5
            except:
                0
        if position.y < -taille[1] + 600:
            position.y = -taille[1] + 600
        if position.y > 0:
            position.y = 0
        if position.x > 0:
            position.x = 0
        if position.x < -taille[0] + 800:
            position.x = -taille[0] + 800


class persobase(Personnage):
    def __init__(self):
        self.B1 = pygame.image.load("perso/N-Ship/B1.png")
        self.B2 = pygame.image.load("perso/N-Ship/B2.png")
        self.B3 = pygame.image.load("perso/N-Ship/B3.png")

        self.F1 = pygame.image.load("perso/N-Ship/F1.png")
        self.F2 = pygame.image.load("perso/N-Ship/F2.png")
        self.F3 = pygame.image.load("perso/N-Ship/F3.png")

        self.R1 = pygame.image.load("perso/N-Ship/R1.png")
        self.R2 = pygame.image.load("perso/N-Ship/R2.png")
        self.R3 = pygame.image.load("perso/N-Ship/R3.png")

        self.L1 = pygame.image.load("perso/N-Ship/L1.png")
        self.L2 = pygame.image.load("perso/N-Ship/L2.png")
        self.L3 = pygame.image.load("perso/N-Ship/L3.png")
        Personnage.__init__(self)

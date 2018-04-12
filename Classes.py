import pygame as pg
from Options import *
vec = pg.math.Vector2

class Spritesheet :
    # classe pour charger et analyser les sprites
    def __init__(self, filename) :
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, l, h):
        # prendre une image depuis un fichier png avec toutes nos images
        image = pg.Surface((l,h))
        image.blit(self.spritesheet, (0, 0), (x, y, l, h))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = self.game.spritesheet.get_image(2, 2, 34, 50)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(10, HAUTEUR/2)
        self.vit = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # on saute seulemnt si l'on est au sol ous ur une plateforme
        self.rect.x+=1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -=1
        if hits :
            self.vit.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # on applique les frottements du sol
        self.acc.x += self.vit.x * PLAYER_FRICTION
        #équations du mouvement
        self.vit += self.acc
        self.pos += self.vit + 0.5 * self.acc

        if self.pos.x <= 20 :
            self.pos.x = 20
        if self.pos.x >= 780 :
            self.pos.x = 780
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, l, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((l, h))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

import pygame as pg
from random import randint
from Options import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.pos = vec(10, HAUTEUR/2)
        self.vit = vec(0, 0)
        self.acc = vec(0, 0)

    def load_images(self) :
        self.standing_frames = [pg.image.load('img/R1.png').convert_alpha()]

        self.walk_frames_r = [pg.image.load('img/R1.png'),
                              pg.image.load('img/R2.png'),
                              pg.image.load('img/R3.png')]
        self.walk_frames_l = []
        for frame in self.walk_frames_r :
            frame.convert_alpha()
            self.walk_frames_l.append(pg.transform.flip(frame, True, False))

        self.jump_frame_r = self.walk_frames_r[2]
        self.jump_frame_l = self.walk_frames_l[2]

    def jump(self):
        # on saute seulemnt si l'on est au sol ous ur une plateforme
        self.rect.x+=1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -=1
        if hits :
            self.vit.y = -PLAYER_JUMP

    def update(self):
        self.animate()
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
        if abs(self.vit.x) < 0.1 :
            self.vit.x = 0
        self.pos += self.vit + 0.5 * self.acc

        if self.pos.x <= 20 :
            self.pos.x = 20
        if self.pos.x >= 780 :
            self.pos.x = 780
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()

        if self.vit.x != 0 :
            self.walking = True
        else :
            self.walking = False

        if self.vit.y != 0 :
            self.jumping = True
        else :
            self.jumping = False

        if self.jumping :
        # animation personnage pendant le saut
            bottom = self.rect.bottom
            if self.vit.x >= 0 :
                self.image = self.jump_frame_r
            else :
                self.image = self.jump_frame_l
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom

        if self.walking and not self.jumping :
            # animation personnage pendant la course
            if now - self.last_update > 180 :
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                bottom = self.rect.bottom
                if self.vit.x > 0 :
                    self.image = self.walk_frames_r[self.current_frame]
                else :
                    self.image = self.walk_frames_l[self.current_frame]
                self.rect =self.image.get_rect()
                self.rect.bottom = bottom

        # animation du personnage lorsqu'il n'y a pas de mouvement
        if not self.jumping and not self.walking :
             if now - self.last_update > 350 :
                 self.last_update = now
                 self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                 bottom = self.rect.bottom
                 self.image = self.standing_frames[self.current_frame]
                 self.rect = self.image.get_rect()
                 self.rect.bottom = bottom

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.create_plat()
        self.image = self.plat_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def create_plat(self) :
        n = int(randint(1, 10))
        rect_img = []
        self.platform = [pg.image.load('img/plateforme1.png')]
        for i in range (1, n+1) :
            self.platform.append(pg.image.load('img/plateforme2.png'))
        self.platform.append(pg.image.load('img/plateforme3.png'))
        self.plat_image = pg.Surface((40+n*20, 20))
        for i in range (0, len(self.platform)) :
            self.platform[i] = self.platform[i].convert_alpha()
            rect_img.append(self.platform[i].get_rect())
            rect_img[i][0] = rect_img[i-1][0]+ rect_img[i-1][2]
            if i == 0 :
                rect_img[i][0] = 0
            self.plat_image.blit(self.platform[i], (rect_img[i][0], 0))

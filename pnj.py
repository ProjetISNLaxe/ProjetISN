import pygame


class pnj(pygame.sprite.Sprite):
    def __init__(self, pnj):
        self.image=pygame.image.load("pnj/"+pnj+"/image")
        self.rect=self.image.get_rect()
        coordfi=open("pnj/"+pnj+"/coord","r")
        self.rect.x=coordfi.read().split(",")[0]
        self.rect.y=coordfi.read().split(",")[1]
        coordfi.close()
    def move(self, masque, position):
        self.x+=5
    def affiche(self, map):
        map.blit(self.image, self.rect)
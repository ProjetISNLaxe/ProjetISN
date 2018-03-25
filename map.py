import pygame
from pygame.locals import *

def map(fenetre, image, image_obstales, perso):
    pygame.key.set_repeat(200, 60)  # Répétition des touches
    clock = pygame.time.Clock()
    position=image.get_rect()
    masque=pygame.mask.from_surface(image_obstales)
    taille=image.get_size()
    position = Rect(-580,-1320,1920,1920)
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pygame.quit()
                    exit()
        perso.eventkey()
        if masque.overlap(perso.mask, (perso.rect.x-position.x, perso.rect.y+perso.size[1]-position.y)):
            perso.allowedT=False
        else:
            perso.allowedT=True
        if masque.overlap(perso.mask, (perso.rect.x-position.x, perso.rect.y-perso.size[1]*2-position.y)):
            perso.allowedB=False
        else:
            perso.allowedB=True
        if masque.overlap(perso.mask, (perso.rect.x+perso.size[0]*2-position.x, perso.rect.y-position.y)):
            perso.allowedR=False
        else:
            perso.allowedR=True
        if masque.overlap(perso.mask, (perso.rect.x-perso.size[0]-position.x, perso.rect.y-position.y)):
            perso.allowedL=False
        else:
            perso.allowedL=True
        fenetre.blit(image, position)
        fenetre.blit(image_obstales, position)
        fenetre.blit(perso.imageperso, perso.rect)
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


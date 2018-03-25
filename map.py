import pygame
from pygame.locals import *

def map(fenetre, image, image_obstales, perso, position):
    pygame.key.set_repeat(200, 60)  # Répétition des touches
    clock = pygame.time.Clock()
    masque=pygame.mask.from_surface(image_obstales)
    taille=image.get_size()
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pygame.quit()
                    exit()
        if perso.rect.y>300 or perso.rect.y<200:
            perso.eventkey()
            for i in range(int(perso.size[1] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - i - position.y)):
                    perso.allowedT = False
                    break
                else:
                    perso.allowedT = True
            for i in range(int(perso.size[1] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y + i - position.y)):
                    perso.allowedD = False
                    break
                else:
                    perso.allowedD = True
            for i in range(int(perso.size[0] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x + i - position.x, perso.rect.y - position.y)):
                    perso.allowedR = False
                    break
                else:
                    perso.allowedR = True
            for i in range(int(perso.size[0] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - i - position.x, perso.rect.y - position.y)):
                    perso.allowedL = False
                    break
                else:
                    perso.allowedL = True
            if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                perso.allowedT = True
                perso.allowedR = True
                perso.allowedL = True
                perso.allowedD = True
        else:
            perso.mapkey(position)
            for i in range(int(perso.size[1] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y-i)):
                    perso.allowedTmap = False
                    break
                else:
                    perso.allowedTmap = True
            for i in range(int(perso.size[1] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y+i)):
                    perso.allowedDmap = False
                    break
                else:
                    perso.allowedDmap = True
            for i in range(int(perso.size[0] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x+i, perso.rect.y - position.y)):
                    perso.allowedRmap = False
                    break
                else:
                    perso.allowedRmap = True
            for i in range(int(perso.size[0] / 3 + 10)):
                if masque.overlap(perso.mask, (perso.rect.x - position.x-i, perso.rect.y - position.y)):
                    perso.allowedLmap = False
                    break
                else:
                    perso.allowedLmap = True
            if masque.overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                perso.allowedTmap = True
                perso.allowedRmap = True
                perso.allowedLmap = True
                perso.allowedDmap = True

        print(perso.rect)
        fenetre.blit(image, position)
        fenetre.blit(image_obstales, position)
        fenetre.blit(perso.imageperso, perso.rect)
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


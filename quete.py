import pygame, random, sys
from pygame.locals import *


def quetes(fenetre):
    activefich=open("quetes\\active", "r")
    active=activefich.read()
    activefich.close()
    if active=="marie":
        marie(fenetre)
    if active=="patrick":
        patrick(fenetre)
def marie(fenetre):
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()
    dragonfi=open("quetes\\marie\\dragon", "r")
    dragon=dragonfi.read()
    dragonfi.close()
    litransifi = open("quetes\\visitelieu", "r")
    lieu=litransifi.read()
    litransifi.close()

    if active=="dragon" and dragon=="0":
        toprintfi=open("quetes\\marie\\toprint", "w")
        toprintfi.write("Effectuez un score de 10 au snake")
        toprintfi.close()
        pygame.image.save(fenetre, "inventory/fond.jpg")
        score= snake(fenetre)
        if score>=10:
            toprintfi = open("quetes\\marie\\toprint", "w")
            toprintfi.write("Allez voir Patrick")
            toprintfi.close()
            dragonfi1 = open("quetes\\marie\\dragon", "w")
            dragonfi1.write("1")
            dragonfi1.close()

    if active == "patrick" and dragon=="1":
        activefich = open("quetes\\active", "w")
        activefich.write("")
        activefich.close()
        dragonfi = open("quetes\\marie\\dragon", "w")
        dragonfi.write("0")
        dragonfi.close()
        toprintfi = open("quetes\\marie\\toprint","w")
        toprintfi.write("Allez voir le dragon")
        toprintfi.close()
        todo=open("quetes\\liste", "w")
        todo.write("patrick")
        todo.close()
def patrick():
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()
    litransifi = open("quetes\\visitelieu", "r")
    lieu=litransifi.read()
    litransifi.close()

    if active == "marie":
        activefich = open("quetes\\active", "w")
        activefich.write("")
        activefich.close()
        toprintfi = open("quetes\\patrick\\toprint","w")
        toprintfi.write("Allez voir Marie")
        toprintfi.close()






def snake(fenetre):
    snakex = [290, 290, 290, 290, 290]
    snakey = [290, 270, 250, 230, 210]
    direction = 0
    score = 0
    pommepos = (random.randint(0, 590), random.randint(0, 590))
    pommeimage = pygame.Surface((10, 10))
    pommeimage.fill((255, 0, 0))
    serpent = pygame.Surface((20, 20))
    serpent.fill((0, 255, 0))
    fond=pygame.image.load("inventory/fond.jpg").convert()
    police = pygame.font.SysFont("monospace", 40)
    clock = pygame.time.Clock()
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != 0:
                    direction = 2
                elif event.key == K_DOWN and direction != 2:
                    direction = 0
                elif event.key == K_LEFT and direction != 1:
                    direction = 3
                elif event.key == K_RIGHT and direction != 3:
                    direction = 1
        i = len(snakex) - 1
        while i >= 2:
            if snakex[0] + 20 > snakex[i] and snakex[0] < snakex[i] + 20 and snakey[0] + 20 > snakey[i] and snakey[0] < snakey[i] + 20:
                return score
            i -= 1
        if snakex[0] + 20 > pommepos[0] and snakex[0] < pommepos[0] + 10 and snakey[0] + 20 > pommepos[1] and snakey[0] < pommepos[1] + 10:
            score += 1
            snakex.append(700)
            snakey.append(700)
            pommepos = (random.randint(0, 590), random.randint(0, 590))
        if snakex[0] < 0 or snakex[0] > 780 or snakey[0] < 0 or snakey[0] > 780: return
        i = len(snakex) - 1
        while i >= 1:
            snakex[i] = snakex[i - 1]
            snakey[i] = snakey[i - 1]
            i -= 1
        if direction == 0:
            snakey[0] += 20
        elif direction == 1:
            snakex[0] += 20
        elif direction == 2:
            snakey[0] -= 20
        elif direction == 3:
            snakex[0] -= 20
        fenetre.blit(fond, (0,0))
        for i in range(0, len(snakex)):
            fenetre.blit(serpent, (snakex[i], snakey[i]))
        fenetre.blit(pommeimage, pommepos)
        fenetre.blit(police.render(str(score), True, (0, 0, 0)), (10, 10))
        pygame.display.flip()

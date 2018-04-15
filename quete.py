import pygame, random, sys
from pygame.locals import *
from imageinterfacetoload import testrect, alphabet, police

def quetes(fenetre):
    activefich = open("quetes\\active", "r")
    active = activefich.read()
    activefich.close()
    if active == "marie":
        marie(fenetre)
    if active == "patrick":
        patrick(fenetre)
    if active == "spawn":
        histoire(fenetre)
    if active == "dragon":
        dragon(fenetre)

def remove(pnj):
    todo = open("quetes\\liste", "r")
    todoli = todo.read().split(",")
    todo.close()
    todoli.remove(pnj)
    for i in range(len(todoli) - 1):
        todoli[i] += ","
    todostr = ""
    for i in range(len(todoli)):
        todostr += todoli[i]
    todo = open("quetes\\liste", "w")
    todo.write(todostr)
    todo.close()
    activefich = open("quetes\\active", "w")
    activefich.write("")
    activefich.close()

def win(pnj, fenetre):
    """Fonction qui permet l'affichage des dialogues pnj perso"""
    clock = pygame.time.Clock()
    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
    winfi = open("quetes/" + pnj + "/win", "r")
    winstr = winfi.read()#On ouvre une liste dans un fichier contenant divers dialogues possibles
    winfi.close()
    imagepnj = pygame.image.load("pnj/" + pnj + "/" + pnj + "_tall.png").convert_alpha()#image du pnj à droite
    bouton2 = pygame.image.load("quetes/HUD/boutonretour.png").convert_alpha()
    bouton2rect = bouton2.get_rect()
    bouton2rect.x = 420
    bouton2rect.y = 545
    quetedispof = open("quetes/quetedispo", "r")
    quetedispo = quetedispof.read().split(",")#On ouvre le fichier de sauvegarde contenant les quêtes disponibles
    quetedispof.close()
    quetefi = open("quetes/active", "r")
    queteactive = quetefi.read()#Quete active
    quetefi.close()
    taillepnj = imagepnj.get_size()
    x = 0
    tobreak = False
    text = winstr
    i = 0
    while 1:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
            if event.type== MOUSEMOTION:
                if event.type == MOUSEMOTION:
                    testrect.x = event.pos[0]
                    testrect.y = event.pos[1]
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if testrect.colliderect(bouton2rect):
                        return
        tobreak = False#Pour casser une boucle
        fenetre.blit(dialoguequete, (0, 374))
        dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
        fenetre.blit(imagepnj, (10, 540 - taillepnj[1]))
        fenetre.blit(bouton2, bouton2rect)
        if len(text) > 65:#Si le texte sort du cadre
            affich = []#liste des lignes à afficher
            k = 0#increment
            motablit = text.split(" ")#On crée un liste avec tout les mots
            for i in range(int(len(text) / 65) + 3):

                affich.append("")
                while len(affich[i]) < 65:#On rajoute des mots
                    if k < len(motablit) - 1:#sauf si le nombre de caractère sort du cadre
                        if len(affich[i] + motablit[k] + " ") < 65:
                            affich[i] += motablit[k] + " "
                        else:
                            break
                        k += 1
                    else:
                        break
            if motablit[-1] not in affich[-1]:#Si le dernier mot est décalé on le reblit dans la dernière phrase
                for i in range(len(alphabet)):
                    for j in range(len(affich)):
                        if alphabet[i] not in affich[j]:
                            affich[j] += motablit[-1]
                            tobreak = True
                            break
                    if tobreak:
                        break
            if len(affich) <= 10:#Si on sort pas du cadre horizontale
                for i in range(len(affich)):#blit normal
                    dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, 10 + 15 * i))
            else:#sinon on crée un curseur

                tkey = pygame.key.get_pressed()
                if tkey[K_UP] and x + 374 + 15 * len(affich) + 25 > 550:

                    x -= 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                elif tkey[K_DOWN] and 384 + x + 10 <= 384:
                    x += 7.5
                    dialoguequete = pygame.image.load("quetes/HUD/boitedialogue.png").convert_alpha()
                for i in range(len(affich)):
                    if x + 384 + 15 * i < 530:
                        dialoguequete.blit(police.render(affich[i], True, (32, 153, 152)), (175, x + 10 + 15 * i))

        if len(text) < 65:
            dialoguequete.blit(police.render(text, True, (32, 153, 152)), (175, 10 + 15 * i))

        clock.tick(60)  # 60 FPS
        pygame.display.flip()



def marie(fenetre):
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()

    if active == "patrick":
        pygame.image.save(fenetre, "inventory/fond.jpg")
        activefich = open("quetes\\pnjrencontre", "w")
        activefich.write("")
        activefich.close()
        remove("marie")
        win("marie", fenetre)

def patrick(fenetre):
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()
    litransifi = open("quetes\\visitelieu", "r")
    lieu = litransifi.read()
    litransifi.close()

    if active == "marie":
        remove("patrick")
        win("patrick", fenetre)

def snake(fenetre):
    snakex = [290, 290, 290, 290, 290]
    snakey = [290, 270, 250, 230, 210]
    direction = 0
    score = 0
    pommepos = (random.randint(100, 690), random.randint(100, 690))
    pommeimage = pygame.Surface((10, 10))
    pommeimage.fill((255, 0, 0))
    serpent = pygame.Surface((20, 20))
    serpent.fill((0, 255, 0))
    fond = pygame.image.load("inventory/screenshot.jpg").convert()
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
            if snakex[0] + 20 > snakex[i] and snakex[0] < snakex[i] + 20 and snakey[0] + 20 > snakey[i] and snakey[0] < \
                    snakey[i] + 20:
                return score
            i -= 1
        if snakex[0] + 20 > pommepos[0] and snakex[0] < pommepos[0] + 10 and snakey[0] + 20 > pommepos[1] and snakey[
            0] < pommepos[1] + 10:
            score += 1
            snakex.append(700)
            snakey.append(700)
            pommepos = (random.randint(100, 690), random.randint(100, 490))
        if snakex[0] < 0 or snakex[0] > 780 or snakey[0] < 0 or snakey[0] > 580:
            return score
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
        fenetre.blit(fond, (0, 0))
        for i in range(0, len(snakex)):
            fenetre.blit(serpent, (snakex[i], snakey[i]))
        fenetre.blit(pommeimage, pommepos)
        fenetre.blit(police.render(str(score), True, (0, 0, 0)), (10, 10))
        pygame.display.flip()

def histoire(fenetre):
    rencontrefi = open("quetes\\pnjrencontre", "r")
    rencontre = rencontrefi.read()
    rencontrefi.close()
    mobfi = open("quetes\\mobmort", "r")
    mob = mobfi.read()
    mobfi.close()
    toprintfi = open("quetes\\histoire\\toprint", "w")
    toprintfi.write("Explorez les environs")
    toprintfi.close()
    jeanmafi = open("quetes\\pnjrencontre", "r")
    jeanma = jeanmafi.read()
    jeanmafi.close()
    if rencontre == "jeanma" and jeanma == "0":
        toprintfi = open("quetes\\histoire\\toprint", "w")
        toprintfi.write("Sauvez-le ou vous serez chatié")
        toprintfi.close()
    if jeanma == "0" and mob == "loup":
        jeanmafi = open("quetes\\pnjrencontre", "r")
        jeanmafi.write("1")
        jeanmafi.close()
    if jeanma == "1":
        toprintfi = open("quetes\\histoire\\toprint", "w")
        toprintfi.write("Cherchez un bateau sur la rive")
        toprintfi.close()

def dragon(fenetre):
    activefich = open("quetes\\pnjrencontre", "r")
    active = activefich.read()
    activefich.close()

    if active == "dragon":
        pygame.image.save(fenetre, "inventory/screenshot.jpg")
        score = snake(fenetre)
        activefich = open("quetes\\pnjrencontre", "w")
        activefich.write("")
        activefich.close()
        if score>10:
            remove("dragon")
            win("dragon",fenetre)
        else:
            return
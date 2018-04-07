import pygame
from pygame.locals import *
from perso_classes import *
import sys
from combatV3 import *
import quete
import time
from printinvent import printinvent

listequetefi = open("quetes\\liste", "r")
listequete = listequetefi.read().split("\'")
listequetefi.close()


def selecmap(fenetre):
    chargement()
    fichier = open("save1\\map", "r")
    mapactive = fichier.read()
    fichier.close()
    if mapactive == "capitale":
        capitale(fenetre)
    if mapactive == "maison_1":
        maison_1(fenetre)
    if mapactive == "maison_2":
        maison_2(fenetre)
    if mapactive == "auberge_1F":
        auberge_1F(fenetre)
    if mapactive == "auberge_2F":
        auberge_2F(fenetre)
    if mapactive == "chateau_1F":
        chateau_1F(fenetre)
    if mapactive == "chateau_2F":
        chateau_2F(fenetre)
    if mapactive == "chateau_3F":
        chateau_3F(fenetre)


def chargement():
    global capitaleload
    capitaleload = False
    global auberge_1Fload
    auberge_1Fload = False
    global chateau_1Fload
    chateau_1Fload = False
    global chateau_2Fload
    chateau_2Fload = False


def capitale(fenetre):
    global capitaleload
    capitaleload = True

    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\capitale\\capitale.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\capitale\\capitale_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\capitale\\capitale_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapcapitale")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\capitale\\spawncapitale")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesocapitale")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\capitale\\transicapitale", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    testtime = 0
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\capitale\\capitale_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\capitale\\pnjcapitale", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\capitale\\capitale_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesocapitale", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapcapitale", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapcapitale", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:
                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):

                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()
                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesocapitale", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapcapitale", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    if transili[i] == "maison_1":
                        maison_1(fenetre)
                        testtime = time.time()
                        break
                    if transili[i] == "maison_2":
                        maison_2(fenetre)
                        testtime = time.time()
                        break
                    if transili[i] == "auberge_1F":
                        auberge_1F(fenetre)
                        testtime = time.time()
                        break
                    if transili[i] == "chateau_1F":
                        chateau_1F(fenetre)
                        testtime = time.time()
                        break
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_1(fenetre):
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\maison_1\\maison_1.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\maison_1\\maison_1_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\maison_1\\maison_1_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapmaison_1")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\maison_1\\spawnmaison_1")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesomaison_1")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\maison_1\\transimaison_1", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\maison_1\\maison_1_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    pnji = open("imgmap\\maison_1\\pnjmaison_1", "r")
    pnj = pnji.read()
    pnji.close()
    pnjli = pnj.split(",")
    imagepnj = []
    maskpnj = []

    for i in range(len(pnjli)):
        imagepnj.append(
            pygame.image.load("imgmap\\maison_1\\maison_1_" + pnjli[i] + ".png"))
        maskpnj.append(pygame.mask.from_surface(imagepnj[i]))

    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesomaison_1", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapmaison_1", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesomaison_1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapmaison_1", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        for i in range(len(pnjli)):
            fenetre.blit(imagepnj[i], position)
            if tkey[K_f]:

                if maskpnj[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):

                    listequetefi = open("quetes\\liste", "r")
                    listequete = listequetefi.read().split("\'")
                    listequetefi.close()

                    if pnjli[i] in listequete:

                        activefich = open("quetes\\active", "r")
                        activeque = activefich.read()
                        activefich.close()

                        if activeque == "":
                            activefich = open("quetes\\active", "w")
                            activefich.write(pnjli[i])
                            activefich.close()

                    activefich = open("quetes\\pnjrencontre", "r")
                    activeque = activefich.read()
                    activefich.close()
                    if activeque != pnjli[i]:
                        activefich = open("quetes\\pnjrencontre", "w")
                        activefich.write(pnjli[i])
                        activefich.close()
                    quete.quetes()
                    break

        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesomaison_1", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapmaison_1", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def maison_2(fenetre):
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\maison_2\\maison_2.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\maison_2\\maison_2_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\maison_2\\maison_2_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapmaison_2")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\maison_2\\spawnmaison_2")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesomaison_2")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\maison_2\\transimaison_2", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\maison_2\\maison_2_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\maison_2\\pnjmaison_2", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\maison_2\\maison_2_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesomaison_2", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapmaison_2", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapmaison_2", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):

                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesomaison_2", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapmaison_2", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_1F(fenetre):
    global auberge_1Fload
    auberge_1Fload = True

    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\auberge_1F\\auberge_1F.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\auberge_1F\\auberge_1F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\auberge_1F\\auberge_1F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapauberge_1F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    testtime = 0
    if carect == "":
        mapactives = str("imgmap\\auberge_1F\\spawnauberge_1F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesoauberge_1F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\auberge_1F\\transiauberge_1F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\auberge_1F\\auberge_1F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\auberge_1F\\pnjauberge_1F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\auberge_1F\\auberge_1F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesoauberge_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapauberge_1F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesoauberge_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapauberge_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesoauberge_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapauberge_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return

                            break

                        else:
                            capitale(fenetre)
                            break
                    if transili[i] == "auberge_2F":
                        auberge_2F(fenetre)
                        testtime = time.time()
                        break

        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def auberge_2F(fenetre):
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\auberge_2F\\auberge_2F.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\auberge_2F\\auberge_2F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\auberge_2F\\auberge_2F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapauberge_2F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\auberge_2F\\spawnauberge_2F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesoauberge_2F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\auberge_2F\\transiauberge_2F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\auberge_2F\\auberge_2F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\auberge_2F\\pnjauberge_2F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\auberge_2F\\auberge_2F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesoauberge_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapauberge_2F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesoauberge_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapauberge_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesoauberge_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapauberge_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global auberge_1Fload
                    if transili[i] == "auberge_1F":
                        if auberge_1Fload:
                            return
                        else:
                            auberge_1F(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_1F(fenetre):
    global chateau_1Fload
    chateau_1Fload = True

    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\chateau_1F\\chateau_1F.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\chateau_1F\\chateau_1F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\chateau_1F\\chateau_1F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapchateau_1F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\chateau_1F\\spawnchateau_1F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])
    testtime = 0
    rectpersoactif = str("save1\\pospeso\\pospesochateau_1F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\chateau_1F\\transichateau_1F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\chateau_1F\\chateau_1F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\chateau_1F\\pnjchateau_1F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\chateau_1F\\chateau_1F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesochateau_1F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapchateau_1F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesochateau_1F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_1F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global capitaleload
                    if transili[i] == "capitale":
                        if capitaleload:
                            return
                        else:
                            capitale(fenetre)
                    if transili[i] == "chateau_2F":
                        chateau_2F(fenetre)
                        testtime = time.time()
                        break
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_2F(fenetre):
    global chateau_2Fload
    chateau_2Fload = True

    testtime = 0
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\chateau_2F\\chateau_2F.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\chateau_2F\\chateau_2F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\chateau_2F\\chateau_2F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapchateau_2F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\chateau_2F\\spawnchateau_2F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesochateau_2F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\chateau_2F\\transichateau_2F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\chateau_2F\\chateau_2F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\chateau_2F\\pnjchateau_2F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\chateau_2F\\chateau_2F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesochateau_2F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapchateau_2F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "inventory\\fond.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e] and time.time() - testtime > 0.5:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesochateau_2F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_2F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global chateau_1Fload
                    if transili[i] == "chateau_1F":
                        if chateau_1Fload:
                            return
                        else:
                            chateau_1F(fenetre)
                    if transili[i] == "chateau_3F":
                        chateau_3F(fenetre)
                        testtime = time.time()
                        break
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS


def chateau_3F(fenetre):
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    image = pygame.image.load("imgmap\\chateau_3F\\chateau_3F.png").convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\chateau_3F\\chateau_3F_obstacle.png").convert_alpha()
    try:
        image_dessus = pygame.image.load("imgmap\\chateau_3F\\chateau_3F_dessus").convert_alpha()
    except:
        None
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = persobase()
    persof.close
    mapactives = str("save1\\posmap\\posmapchateau_3F")
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect == "":
        mapactives = str("imgmap\\chateau_3F\\spawnchateau_3F")
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospesochateau_3F")
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400 - perso.size[0] / 2
        perso.rect.y = 300 - perso.size[1] / 2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi = open("imgmap\\chateau_3F\\transichateau_3F", "r")
    transition = transi.read()
    transi.close()
    transili = transition.split(",")
    imagetransi = []
    masktransi = []
    for i in range(len(transili)):
        imagetransi.append(
            pygame.image.load("imgmap\\chateau_3F\\chateau_3F_" + transili[i] + ".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
    try:
        pnji = open("imgmap\\chateau_3F\\pnjchateau_3F", "r")
        pnj = pnji.read()
        pnji.close()
        pnjli = pnj.split(",")
        imagepnj = []
        maskpnj = []

        for i in range(len(pnjli)):
            imagepnj.append(
                pygame.image.load("imgmap\\chateau_3F\\chateau_3F_" + pnjli[i] + ".png"))
            maskpnj.append(pygame.mask.from_surface(imagepnj[i]))
    except:
        None
    myfont = pygame.font.SysFont("monospace", 20)
    grandemap = pygame.image.load("imgmap\\map.png").convert_alpha()

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospesochateau_3F", "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmapchateau_3F", "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_3F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    return
                if event.key == K_i:
                    pygame.image.save(fenetre, "\\screenshot.jpg")
                    printinvent(fenetre)
        perso.eventkey(position, masque, taille)
        tkey = pygame.key.get_pressed()

        for i in range(len(transili)):
            if masktransi[i].overlap(perso.mask, (perso.rect.x - position.x, perso.rect.y - position.y)):
                affichetext = True
                break
            else:
                affichetext = False

        goldf = open("save1\\invent\\cpic")
        perso.gold = int(goldf.read())
        goldf.close()
        fenetre.blit(image, position)

        try:
            for i in range(len(pnjli)):
                fenetre.blit(imagepnj[i], position)
                if tkey[K_f]:

                    if maskpnj[i].overlap(perso.mask,
                                          (perso.rect.x - position.x, perso.rect.y - position.y)):
                        listequetefi = open("quetes\\liste", "r")
                        listequete = listequetefi.read().split("\'")
                        listequetefi.close()

                        if pnjli[i] in listequete:
                            activefich = open("quetes\\active", "r")
                            activeque = activefich.read()
                            activefich.close()
                            if activeque == "":
                                activefich = open("quetes\\active", "w")
                                activefich.write(pnjli[i])
                                activefich.close()

                        activefich = open("quetes\\pnjrencontre", "r")
                        activeque = activefich.read()
                        activefich.close()
                        if activeque != pnjli[i]:
                            activefich = open("quetes\\pnjrencontre", "w")
                            activefich.write(pnjli[i])
                            activefich.close()
                        quete.quetes()
                        break
        except:
            None
        fenetre.blit(perso.imageperso, perso.rect)
        try:
            fenetre.blit(image_dessus, position)
        except:
            None

        if tkey[K_e]:
            for i in range(len(transili)):
                if masktransi[i].overlap(perso.mask,
                                         (perso.rect.x - position.x, perso.rect.y - position.y)):
                    maptransi = open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso = open("save1\\pospeso\\pospesochateau_3F", "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmapchateau_3F", "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    fenetre.blit(myfont.render("CHARGEMENT...", False, (1, 44, 166)), (500, 50))
                    pygame.display.flip()
                    litransifi = open("quetes\\visitelieu", "w")
                    litransifi.write(transili[i])
                    litransifi.close()
                    quete.quetes()
                    global chateau_2Fload
                    if transili[i] == "chateau_2F":
                        if chateau_2Fload:
                            return
                        else:
                            chateau_2F(fenetre)
        if affichetext:
            fenetre.blit(myfont.render("PRESS E", False, (1, 44, 166)), (perso.rect.x - 75, perso.rect.y))
        if tkey[K_SEMICOLON]:
            fenetre.blit(grandemap, (0, 0))
            fenetre.blit(perso.imageperso, (192, 194))
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS

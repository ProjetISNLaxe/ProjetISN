import pygame
from pygame.locals import *
from perso_classes import Personnage


def map(fenetre):
 while 1:
    pygame.key.set_repeat(200, 100)  # Répétition des touches
    clock = pygame.time.Clock()
    mapactivef = open("save1\\map", "r")
    mapactivet = mapactivef.read()
    mapactivez=mapactivet
    mapactives = mapactivet
    mapactive_obstaclet = mapactivet + "_obstacle"
    mapactivet = mapactivet + ".png"
    mapactive_obstaclet = mapactive_obstaclet + ".png"
    mapactivef.close()
    image = pygame.image.load("imgmap\\" +mapactivez+"\\"+ mapactivet).convert_alpha()
    image_obstacles = pygame.image.load("imgmap\\" +mapactivez+"\\"+ mapactive_obstaclet).convert_alpha()
    position = image.get_rect()
    persof = open("save1\\perso", "r")
    person = persof.read()
    if person == "1":
        perso = Personnage()
    persof.close
    mapactives = str("save1\\posmap\\posmap" + mapactivez)
    rectf = open(mapactives, "r")
    carect = rectf.read()
    rectf.close()
    if carect=="":
        mapactives = str("imgmap\\"+mapactivez+"\\spawn" + mapactivez)
        rectf = open(mapactives, "r")
        carect = rectf.read()
        rectf.close()
    lirect = carect.split(",")
    position.x = int(lirect[0])
    position.y = int(lirect[1])

    rectpersoactif = str("save1\\pospeso\\pospeso" + mapactivez)
    rectpersof = open(rectpersoactif, "r")
    shaperso = rectpersof.read()
    rectpersof.close()
    if shaperso == "":
        perso.rect.x = 400-perso.size[0]/2
        perso.rect.y = 300-perso.size[1]/2
    else:
        lipersorect = shaperso.split(",")
        perso.rect.x = int(lipersorect[0])
        perso.rect.y = int(lipersorect[1])

    masque = pygame.mask.from_surface(image_obstacles)
    taille = image.get_size()

    transi=open("imgmap\\"+mapactivez+"\\transi"+mapactivez, "r")
    transition=transi.read()
    transi.close()
    transili=transition.split(",")
    imagetransi=[]
    masktransi=[]
    recttransi=[]
    end=False
    for i in range (len(transili)):
        imagetransi.append(pygame.image.load("imgmap\\"+mapactivez+"\\"+mapactivez+"_"+transili[i]+".png"))
        masktransi.append(pygame.mask.from_surface(imagetransi[i]))
        recttransi.append(position)

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # quitter le jeux en cliquant sur la croix
                pospeso = open("save1\\pospeso\\pospeso" + mapactivez, "w")
                pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                pospeso.close()
                posmap = open("save1\\posmap\\posmap" + mapactivez, "w")
                posmap.write(str(position.x) + "," + str(position.y))
                posmap.close()
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Echap pour quitter
                    pospeso = open("save1\\pospeso\\pospeso" + mapactivez, "w")
                    pospeso.write(str(perso.rect.x) + "," + str(perso.rect.y))
                    pospeso.close()
                    posmap = open("save1\\posmap\\posmap" + mapactivez, "w")
                    posmap.write(str(position.x) + "," + str(position.y))
                    posmap.close()
                    pygame.quit()
                    exit()
        perso.eventkey(position, masque, taille)
        tkey=pygame.key.get_pressed()
        if tkey[K_f]:
            for i in range (len(transili)):
                if masktransi[i].overlap(perso.mask,(perso.rect.x - recttransi[i].x, perso.rect.y - recttransi[i].y)):
                    maptransi=open("save1\\map", "w")
                    maptransi.write(transili[i])
                    maptransi.close()
                    pospeso=open("save1\\pospeso\\pospeso"+mapactivez, "w")
                    pospeso.write(str(perso.rect.x)+","+str(perso.rect.y))
                    pospeso.close()
                    posmap=open("save1\\posmap\\posmap"+mapactivez, "w")
                    posmap.write(str(position.x)+","+str(position.y))
                    posmap.close()
                    end=True
                    break
        if end==True:
            break
        print(perso.rect)
        fenetre.blit(image, position)
        fenetre.blit(perso.imageperso, perso.rect)
        pygame.display.flip()  # On raffraichis l'ecran
        clock.tick(60)  # 60 FPS




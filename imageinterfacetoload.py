import pygame


interfaceinvent=pygame.image.load("inventory/interface_inventaire_objets.png").convert_alpha()

emplacementperso0=pygame.image.load("inventory/emplacementperso0.png").convert_alpha()
perso0=pygame.image.load("perso/F1.png").convert_alpha()
stuff_actuel=pygame.image.load("inventory/stuff_actuel.png").convert_alpha()
curseur=pygame.image.load("inventory/curseur.png").convert_alpha()
test = pygame.image.load("launcher\pixelgitan.png").convert_alpha()
testrect=test.get_rect()
curseurrect=curseur.get_rect()
testmask=pygame.mask.from_surface(test)
curseurmask=pygame.mask.from_surface(curseur)

police=pygame.font.SysFont("monospace", 15)
objetinventairerect = []
listechiffre = []
taillechiffre= []
for i in range (10):
    listechiffre.append(pygame.image.load("inventory/chiffre/chiffre0"+str(i)+".png").convert_alpha())
    taillechiffre.append(listechiffre[i].get_size())
consommable=["pomme","nbsoin", "mana", "nbresurect"]


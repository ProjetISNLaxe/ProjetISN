import pygame
from pygame.locals import *
from random import *
import random
import time

pygame.init()
fenetre = pygame.display.set_mode((800, 600))


class attaqueennemi():
    def __init__(self):
        self.p = 0

    def cible(self):
        if not sinatra.active:
            n = [1, 2]
        else:
            n = [1, 2, 3]
        if david.vie == 0:
            n[1] = 0
        if perso_joueur.vie == 0:
            n[0] = 0
        if sinatra.vie == 0 and sinatra.active:
            n[2] = 0
        self.p = choice(n)
        while self.p == 0:
            self.p = choice(n)

    def verification(self):
        if malarich.feu > 0:
            malarich.feu -= 1
            david.vie -= 10
            perso_joueur.vie -= 10
            sinatra.vie -= 10
        if david.vie <= 0:
            david.alive = False
            david.vie = 0
        if perso_joueur.vie <= 0:
            perso_joueur.alive = False
            perso_joueur.vie = 0
        if sinatra.vie <= 0:
            sinatra.alive = False
            sinatra.vie = 0
        if sinatra.active:
            if sinatra.vie == 0 and david.vie == 0 and perso_joueur.vie == 0:
                pygame.quit()
                exit()
        elif david.vie == 0 and perso_joueur.vie == 0:
            pygame.quit()
            exit()


class menu:
    def __init__(self):
        self.menu_ = 0


class sac:
    def __init__(self, q, image):
        self.quantite = q
        self.imageanim = pygame.image.load(image).convert_alpha()


class bataille:
    def __init__(self):
        self.etat = "combatencour"
        self.anim = 0
        self.tour = 1


class perso(pygame.sprite.Sprite):
    def __init__(self, imageperso, imageperso2):
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.image2 = pygame.image.load(imageperso2).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.alive = True
        self.niveau = 1
        self.xp = 0
        self.difficulteniveau = self.niveau / 0.75 * 100
        self.ptdecompetance = 0
        self.ptforce = 0
        self.ptvie = 0
        self.bonus = 0
        self.ingame = False
        if self.xp == self.difficulteniveau:
            self.xp = 0
            self.niveau += 1


class perso1(perso):
    def __init__(self):
        perso.__init__(self, "imagebonhomme/joueur/combivaisseau/Perso1nship0.png",
                       "imagebonhomme/joueur/combivaisseau/Perso1nship1.png")
        self.vie = 150
        self.mana = 100
        self.fleche = 0
        self.armure = 0
        self.ptmana = 0
        self.bonusmagique = 0
        self.sortdefeu = False


class perso2(perso):
    def __init__(self):
        perso.__init__(self, "imagebonhomme/perso2/perso2base0.png", "./imagebonhomme/perso2/perso2base1.png")
        self.vie = 200
        self.taunt = 0
        self.armure = 10
        self.ptbouclier = 0
        self.immortal = False


class perso3(perso):
    def __init__(self):
        perso.__init__(self, "imagebonhomme/perso3/perso3armurebase.png",
                       "imagebonhomme/perso3/perso3armurebase2.png")
        self.vie = 100
        self.active = False
        self.poison = False
        self.ptdodge = 0


class affichage():
    def __init__(self):
        0

    def affichageanimennemi(self, d):
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("Battlebacks/005-Beach01.jpg")
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont("Calibri", 36)
        bandeaubleue = pygame.image.load("animation/Fightblue.png").convert_alpha()
        bandeaurouge = pygame.image.load("animation/Fightred.png").convert_alpha()
        i = 0
        fenetre.blit(fond, (0, 0))
        while i < 42:
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (811 - i * 10, 200))
            fenetre.blit(bandeaurouge, (-421 + i * 10, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()
        i = 0
        while i < 160:
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (390, 200))
            fenetre.blit(bandeaurouge, (-1, 200))
            if i < 80:
                if fennemi.p == 2 or david.taunt > 0:
                    fenetre.blit(david.image, (659, 200))
                elif fennemi.p == 1:
                    fenetre.blit(perso_joueur.image, (659, 200))
                elif fennemi.p == 3:
                    fenetre.blit(sinatra.image, (659, 200))
                fenetre.blit(enemitipe.image, (11 + i * 4, 200))
            if i > 80:
                fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
                fenetre.blit(enemitipe.image, (411, 200))
                if fennemi.p == 2 or david.taunt > 0:
                    fenetre.blit(david.image, (689, 200))
                elif fennemi.p == 1:
                    fenetre.blit(perso_joueur.image, (659, 200))
                elif fennemi.p == 3:
                    fenetre.blit(sinatra.image, (659, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()

    def affichage(self, action, choix):
        my_font = pygame.font.SysFont("Calibri", 18)  # les different taille d'ecriture
        my_font2 = pygame.font.SysFont("Calibri", 21)
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("Battlebacks/005-Beach01.jpg")

        position1 = (610, 180)  # la position du perso qui jou
        position2 = (625, 100)  # la position du perso qui attent
        position3 = (640, 20)  # la position du perso qui attent
        positionpv1 = (760, 180)  # la position des pv du perso qui jou
        positionpv2 = (760, 100)  # la position des pv du perso qui attend
        positionpv3 = (760, 20)  # la position des pv du perso qui attend
        position_ennemi1 = (100, 100)

        fenetre.blit(fond, (0, 0))
        for i in range(4):
            fenetre.blit(my_font.render(action[i], False, (255, 255, 255)), (530, 500 + i * 20))

        fenetre.blit(my_font2.render(str(enemitipe.vie), False, (255, 255, 255)), (40, 60))
        if combat.tour == 1:
            fenetre.blit(my_font.render(str(perso_joueur.mana), False, (255, 255, 255)), (80, 500))
            fenetre.blit(my_font.render(str(perso_joueur.fleche), False, (255, 255, 255)), (80, 520))
            fenetre.blit(my_font.render("mana:", False, (255, 255, 255)), (20, 500))
            fenetre.blit(my_font.render("fleches:", False, (255, 255, 255)), (20, 520))
        if objet.menu_ == 1:
            fenetre.blit(my_font.render(str(soin.quantite), False, (255, 255, 255)), (670, 520))
            fenetre.blit(my_font.render(str(resurection.quantite), False, (255, 255, 255)), (670, 500))
            fenetre.blit(my_font.render(str(mana.quantite), False, (255, 255, 255)), (670, 540))
        if combat.tour == 1:
            if not sinatra.active:
                david.rect = position2  # endroit de spawn du perso
                perso_joueur.rect = position1
            else:
                sinatra.rect = position3
                david.rect = position2  # endroit de spawn du perso
                perso_joueur.rect = position1
            if sinatra.active:
                fenetre.blit(sinatra.image, sinatra.rect)
            fenetre.blit(david.image, david.rect)
            fenetre.blit(perso_joueur.image, perso_joueur.rect)

            fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv1)
            fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv2)
            if sinatra.active:
                fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv3)

        if combat.tour == 2:
            if not sinatra.active:
                david.rect = position1  # endroit de spawn du perso
                perso_joueur.rect = position2
            else:
                sinatra.rect = position2
                david.rect = position1  # endroit de spawn du perso
                perso_joueur.rect = position3
            fenetre.blit(perso_joueur.image, perso_joueur.rect)
            if sinatra.active:
                fenetre.blit(sinatra.image, sinatra.rect)
            fenetre.blit(david.image, david.rect)
            fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv1)
            if sinatra.active:
                fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv3)
                fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv2)
            else:
                fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv2)
        if combat.tour == 3:
            david.rect = position3  # endroit de spawn du perso
            perso_joueur.rect = position2
            sinatra.rect = position1
            fenetre.blit(david.image, david.rect)
            fenetre.blit(perso_joueur.image, perso_joueur.rect)
            fenetre.blit(sinatra.image, sinatra.rect)
            fenetre.blit(my_font2.render(str(perso_joueur.vie), False, (255, 255, 255)), positionpv2)
            fenetre.blit(my_font2.render(str(sinatra.vie), False, (255, 255, 255)), positionpv1)
            fenetre.blit(my_font2.render(str(david.vie), False, (255, 255, 255)), positionpv3)

        fenetre.blit(enemitipe.image, position_ennemi1)
        if choix == 1:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 500))
        elif choix == 2:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 520))
        elif choix == 3:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 540))
        elif choix == 4:
            fenetre.blit(my_font.render("-", False, (255, 255, 255)), (520, 560))
        pygame.display.flip()

    def affichageanim(self, d):
        fichier = open("save1/map", "r")
        map = fichier.read()
        fichier.close()

        if map == "capitale":
            fond = pygame.image.load("Battlebacks/009-CastleTown01.jpg")
        elif map == "chateau_3F":
            fond = pygame.image.load("Battlebacks/026-Castle02.jpg")
        elif map == "caverne":
            fond = pygame.image.load("Battlebacks/043-Cave01.jpg")
        elif map == "mapdepart":
            fond = pygame.image.load("Battlebacks/005-Beach01.jpg")
        clock = pygame.time.Clock()
        my_font = pygame.font.SysFont("Calibri", 36)
        bandeaubleue = pygame.image.load("animation/Fightblue.png").convert_alpha()
        bandeaurouge = pygame.image.load("animation/Fightred.png").convert_alpha()
        fouldebeu = pygame.image.load("animation/fireball.png").convert_alpha()
        fouldebeunul = pygame.image.load("animation/fireballkitomb.png").convert_alpha()
        fleche = pygame.image.load("animation/fleche.png").convert_alpha()
        bouclier = pygame.image.load("animation/bouclier.png").convert_alpha()

        i = 0
        fenetre.blit(fond, (0, 0))
        while i < 42:
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (811 - i * 10, 200))
            fenetre.blit(bandeaurouge, (-421 + i * 10, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()

        i = 0
        while i < 160:
            fenetre.blit(fond, (0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (390, 200))
            fenetre.blit(bandeaurouge, (-1, 200))
            if combat.anim == 1 or combat.anim == 3 or combat.anim == 6 or combat.anim == 7 or combat.anim == 8:
                if combat.tour == 1:
                    fenetre.blit(perso_joueur.image, (689, 200))
                if combat.tour == 2:
                    fenetre.blit(david.image, (689, 200))
                if combat.tour == 3:
                    fenetre.blit(sinatra.image, (689, 200))
                fenetre.blit(enemitipe.image, (11, 200))
                if i < 80:
                    if combat.anim == 1:
                        fenetre.blit(fouldebeu, (689 - i * 6, 250))
                    elif combat.anim == 3:
                        fenetre.blit(fleche, (689 - i * 6, 250))
                    elif combat.anim == 6:
                        fenetre.blit(mana.imageanim, (640, 250 - i))
                    elif combat.anim == 7:
                        fenetre.blit(soin.imageanim, (640, 250 - i))
                    elif combat.anim == 8:
                        fenetre.blit(resurection.imageanim, (640, 250 - i))

                else:
                    if combat.anim == 6:
                        fenetre.blit(my_font.render("50", 3, (0, 0, 200)), (680, 180))
                    elif combat.anim == 7:
                        fenetre.blit(my_font.render("50", 3, (0, 200, 0)), (680, 180))
                    elif combat.anim == 8:
                        fenetre.blit(my_font.render("Les allié sont en vie enfin si ca bugue pas", 3, (0, 200, 200)),
                                     (680, 180))
                    else:
                        fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))
            elif combat.anim == 2:
                fenetre.blit(perso_joueur.image, (689, 200))
                fenetre.blit(enemitipe.image, (11, 200))
                if i < 20:
                    fenetre.blit(fouldebeu, (689 - i * 6, 250))
                else:
                    fenetre.blit(fouldebeunul, (569, 250 + i * 2))
            elif combat.anim == 4:
                fenetre.blit(david.image, (689, 200))
            elif combat.anim == 5:
                fenetre.blit(david.image, (689, 200))
                fenetre.blit(bouclier, (689, 200))

            else:
                if i < 80:
                    if combat.tour == 1:
                        fenetre.blit(perso_joueur.image, (689 - i * 4, 200))
                    if combat.tour == 2:
                        fenetre.blit(david.image, (689 - i * 4, 200))
                    if combat.tour == 3:
                        fenetre.blit(sinatra.image, (689 - i * 4, 200))
                if i > 80:
                    if combat.tour == 1:
                        fenetre.blit(perso_joueur.image2, (289, 200))
                    if combat.tour == 2:
                        fenetre.blit(david.image2, (289, 200))
                    if combat.tour == 3:
                        fenetre.blit(sinatra.image2, (289, 200))
                    fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))
            fenetre.blit(enemitipe.image, (11, 200))

            clock.tick(60)
            pygame.display.flip()
            i += 1


class ennemi(pygame.sprite.Sprite):
    def __init__(self, imageperso):
        self.image = pygame.image.load(imageperso).convert_alpha()
        self.rect = self.image.get_rect()
        self.alive = False


class loup(ennemi):
    def __init__(self, imageperso):
        ennemi.__init__(self, imageperso)
        self.vie = 250

    def attaque(self):
        fennemi.cible()
        d = randint(35, 50)
        if david.taunt > 0:
            david.vie -= (d - david.armure)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d)
        fennemi.verification()


class soldatpt(ennemi):
    def __init__(self, imageperso):
        ennemi.__init__(self, imageperso)
        self.vie = 200

    def attaque(self):
        fennemi.cible()
        d = randint(200, 300)
        if david.taunt > 0:
            david.vie -= (d - david.armure)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d)
        fennemi.verification()


class malarich(ennemi):
    def __init__(self, imageperso):
        ennemi.__init__(self, imageperso)
        self.vie = 1000
        self.feu = 0

    def attaque(self):
        fennemi.cible()
        u = randint(0, 2)
        u=2
        if u == 1:
            d = randint(50, 60)
        elif u == 2:
            d = 10
            if fennemi.p == 2:
                lvie = list(str(david.vie))
            elif fennemi.p == 1:
                lvie = list(str(perso_joueur.vie))
            elif fennemi.p == 3:
                lvie = list(str(sinatra.vie))
            if len(lvie)!=0:
                0
            random.shuffle(lvie)
            for i in range(2):
                if lvie[0]=="0":
                    del lvie[0]
            for i in range (len(lvie)):
                str + lvie[i]
            if fennemi.p == 2:
                david.vie = int(lvie)
            elif fennemi.p == 1:
                perso_joueur.vie = int(lvie)
            elif fennemi.p == 3:
                sinatra.vie = int(lvie)
        if u == 0:
            self.feu = 3
            d = 0

        if david.taunt > 0:
            david.vie -= (d - david.armure)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d)
        fennemi.verification()


fichier = open("quetes/mobmort", "r")
nomennemie = fichier.read()
fichier.close()
perso_joueur = perso1()
david = perso2()
sinatra = perso3()
loup = loup("imagebonhomme/ennemi/cerberus.png")
soldat = soldatpt("mob/soldier.png")
malarich = malarich("mob/darklord.png")
base = menu()
objet = menu()
attaque = menu()
soin = sac(1, "animation/nbsoin.png")
resurection = sac(1, "animation/nbresurect.png")
mana = sac(1, "animation/mana.png")
combat = bataille()
enemitipe = ennemi("imagebonhomme/ennemi/cerberus.png")
fennemi = attaqueennemi()
affichage = affichage()

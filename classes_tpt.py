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
        if david.taunt!=0 and david.vie!=0:
            self.p=2
        while self.p == 0:
            self.p = choice(n)

    def verification(self):
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
                combat.etat = "mort"
                pygame.quit()
                exit()
        elif david.vie == 0 and perso_joueur.vie == 0:
            combat.etat = "mort"
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
        self.ptdecompetance = 0
        self.ptforce = 0
        self.ptvie = 0
        self.bonus = 0
        self.ingame = False
        self.empoisoner = 0
        if self.xp == 50 * self.niveau:
            self.xp -= 50 * self.niveau
            self.niveau += 1
            self.ptdecompetance += 1


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
        self.viemax = 150 + (self.ptvie * 20)
        if self.ptmana == 1:
            self.sortdefeu = True
        if self.ptmana > 1:
            self.bonusmagique += 1


class perso2(perso):
    def __init__(self):
        perso.__init__(self, "imagebonhomme/perso2/perso2base0.png", "./imagebonhomme/perso2/perso2base1.png")
        self.vie = 200
        self.taunt = 0
        self.armure = 10
        self.ptbouclier = 0
        self.immortal = False
        self.viemax = 200 + (self.ptvie * 20)


class perso3(perso):
    def __init__(self):
        perso.__init__(self, "imagebonhomme/perso3/perso3armurebase.png",
                       "imagebonhomme/perso3/perso3armurebase2.png")
        self.vie = 100
        self.active = False
        self.poison = False
        self.ptdodge = 0
        self.viemax = 150 + (self.ptvie * 20)


class affichage():
    def __init__(self):
        0

    def affichageanimennemi(self, d, varanim):
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
        pointinterro = pygame.image.load("animation/pointintero.png").convert_alpha()
        feu = pygame.image.load("animation/fire.png").convert_alpha()
        feus=pygame.mixer.Sound("bruit/Fire1.ogg")
        malediction = pygame.image.load("animation/malediction.png").convert_alpha()
        damage = pygame.mixer.Sound("bruit/Damage2.ogg")
        fenetre.blit(fond, (0, 0))
        for i in range (42):
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (811 - i * 10, 200))
            fenetre.blit(bandeaurouge, (-421 + i * 10, 200))
            i += 1
            clock.tick(60)
            pygame.display.flip()
        for i in range(160):
            for event in pygame.event.get():
                if event.type == QUIT:  # pour pouvoir quitter le jeux
                    pygame.quit()
                    exit()
            fenetre.blit(bandeaubleue, (390, 200))
            fenetre.blit(bandeaurouge, (-1, 200))

            if i < 80:
                if varanim!=3 and varanim!=4 :
                    if fennemi.p == 2 or david.taunt > 0:
                        fenetre.blit(david.image, (659, 200))
                    elif fennemi.p == 1:
                        fenetre.blit(perso_joueur.image, (659, 200))
                    elif fennemi.p == 3:
                        fenetre.blit(sinatra.image, (659, 200))
                if varanim==1:
                        fenetre.blit(enemitipe.image, (11, 200))
                elif varanim==2:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(pointinterro, (11, 100))
                elif varanim==3:
                    fenetre.blit(sinatra.image, (640, 70))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(feu, (600, 150))

                elif varanim==4:
                    fenetre.blit(sinatra.image, (640, 70))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(malediction, (600, 150))
                elif varanim==5:
                        fenetre.blit(enemitipe.image, (11, 200))
                elif varanim==0:
                        fenetre.blit(enemitipe.image, (11 + i * 4, 200))
            if i==80:
                if varanim==0:
                    damage.play()
                if varanim==3:
                    feus.play()
            if i > 80:
                if varanim!=3 and varanim!=4 :
                    if fennemi.p == 2 or david.taunt > 0:
                        fenetre.blit(david.image, (689, 200))
                    elif fennemi.p == 1:
                        fenetre.blit(perso_joueur.image, (659, 200))
                    elif fennemi.p == 3:
                        fenetre.blit(sinatra.image, (659, 200))
                else:
                    fenetre.blit(sinatra.image, (640, 70))
                    fenetre.blit(david.image, (625, 150))
                    fenetre.blit(perso_joueur.image, (610, 230))
                if varanim == 1:
                    fenetre.blit(enemitipe.image, (11, 200))
                elif varanim==2:
                    fenetre.blit(enemitipe.image, (11, 200))
                    if d>0:
                        fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
                    elif d<0:
                        fenetre.blit(my_font.render(str(-d), 3, (10, 255, 10)), (659, 180))
                    elif d==0:
                        fenetre.blit(my_font.render(str(d), 3, (10, 10, 10)), (659, 180))
                elif varanim == 3:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(my_font.render(str(d)+"*3", 3, (255, 10, 10)), (659, 180))
                elif varanim == 4:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(malediction, (600, 150))
                elif varanim == 5:
                    fenetre.blit(enemitipe.image, (11, 200))
                    fenetre.blit(my_font.render("1000", 3, (100, 255, 10)), (30, 180))
                elif varanim==0:
                    fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (659, 180))
                    fenetre.blit(enemitipe.image, (411, 200))



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
        damage= pygame.mixer.Sound("bruit/Damage2.ogg")
        potion=pygame.mixer.Sound("bruit/Heal3.ogg")
        feu = pygame.mixer.Sound("bruit/Fire1.ogg")



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
                elif i==80:
                    if combat.anim == 6 or combat.anim == 7 or combat.anim == 8:
                        potion.play()
                    if combat.anim==1:
                        feu.play()

                else:
                    if combat.anim == 6:
                        fenetre.blit(my_font.render("50", 3, (0, 0, 200)), (680, 180))

                    elif combat.anim == 7:
                        fenetre.blit(my_font.render("50", 3, (0, 200, 0)), (680, 180))
                    elif combat.anim == 8:
                        fenetre.blit(my_font.render("Les allié sont en vie", 3, (0, 200, 200)),
                                     (680, 180))
                    else:
                        fenetre.blit(my_font.render(str(d), 3, (255, 10, 10)), (41, 180))
                        damage.play()
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
                if i==80:
                    damage.play()
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
    def __init__(self):
        ennemi.__init__(self, "imagebonhomme/ennemi/cerberus.png")
        self.vie = 250

    def attaque(self):
        fennemi.cible()
        d = randint(35, 50)
        varanim = 0
        if david.taunt > 0:
            david.vie -= (d - david.armure)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class avalogne(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/Imp.png")
        self.vie = 200

    def attaque(self):
        for i in range(2):
            fennemi.cible()
            d = randint(35, 40)
            varanim = 0
            if david.taunt > 0:
                david.vie -= (d - david.armure)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
            affichage.affichageanimennemi(d, varanim)
            fennemi.verification()


class soldatpt(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/soldier.png")
        self.vie = 200

    def attaque(self):
        fennemi.cible()
        d = randint(200, 300)
        varanim = 0
        if david.taunt > 0:
            david.vie -= (d - david.armure)
        elif fennemi.p == 2:
            if not david.immortal:
                david.vie -= (d - david.armure)
        elif fennemi.p == 1:
            perso_joueur.vie -= (d - perso_joueur.armure)
        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class malarich(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/darklord.png")
        self.vie = 1000

    def attaque(self):
        fennemi.cible()
        u = randint(0, 2)
        varanim = 0
        print(u)


        if u == 1:
            if random.random() <= 0.1:
                d = 100
            elif random.random() <= 0.001:
                d = 1000
            else:
                d = randint(70, 80)
        elif u == 2:
            if fennemi.p == 2:
                lvie = list(str(david.vie))
            elif fennemi.p == 1:
                lvie = list(str(perso_joueur.vie))
            elif fennemi.p == 3:
                lvie = list(str(sinatra.vie))
            if len(lvie) != 3:
                a=3-len(lvie)
                for i in range(a):
                    lvie.append("0")
            random.shuffle(lvie)

            l = int(lvie[0]) * 100 + int(lvie[1]) * 10 + int(lvie[2])
            if fennemi.p == 2:
                d=david.vie-l
            elif fennemi.p == 1:
                d = perso_joueur.vie - l
            elif fennemi.p == 3:
                d = sinatra.vie - l
            varanim = 2
            print(david.vie,perso_joueur.vie)
        if u == 0:
            d=30
            varanim = 3
        if varanim==3:
            david.vie -= d
            perso_joueur.vie -= d
            sinatra.vie -= d
        else:
            if david.taunt > 0:
                    if varanim==2:
                        david.vie -= d
                    elif david.armure < d:
                        david.vie -= (d - david.armure)
            elif fennemi.p == 2:
                if not david.immortal:
                    if varanim==2:
                        david.vie -= d
                    elif david.armure < d:
                        david.vie -= (d - david.armure)

            elif fennemi.p == 1:
                if varanim == 2:
                    perso_joueur.vie -= d
                elif perso_joueur.armure < d:
                    perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if varanim==2:
                    sinatra.vie -= d
                elif random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class voleur(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/Rogue.png")
        self.vie = 120
        self.poison = 0

    def attaque(self):
        fennemi.cible()
        u = randint(0, 1)
        varanim = 0
        if u == 0:
            d = randint(35, 40)
            if david.taunt > 0:
                david.vie -= (d - david.armure)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
        else:
            d = 0
            varanim=5
            if david.taunt > 0:
                david.empoisonner = 3
            elif fennemi.p == 2:
                david.empoisonner = 3
            elif fennemi.p == 1:
                perso_joueur.empoisonner = 3
        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()


class hornet(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/Hornet.png")
        self.vie = 200

    def attaque(self):
        for i in range(2):
            fennemi.cible()
            d = randint(25, 30)
            varanim = 0
            if david.taunt > 0:
                david.vie -= (d - david.armure)
            elif fennemi.p == 2:
                if not david.immortal:
                    david.vie -= (d - david.armure)
            elif fennemi.p == 1:
                perso_joueur.vie -= (d - perso_joueur.armure)
            elif fennemi.p == 3:
                if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                    sinatra.vie -= d
            affichage.affichageanimennemi(d, varanim)
            fennemi.verification()

class goddess(ennemi):
    def __init__(self):
        ennemi.__init__(self, "mob/Goddess.png")
        self.vie = 3000
        self.malediction=0

    def attaque(self):
        varanim=0
        fennemi.cible()
        if self.vie<=1000:
            self.vie+=1000
            d=0
            varanim = 5
            sinatra.poison=False
        elif self.malediction==0:
            self.malediction=5
            d=0
            varanim = 4
        elif fennemi.p==2 and david.vie>=david.viemax/2:
            d=david.vie/2
        elif fennemi.p==1 and perso_joueur.vie>=perso_joueur.viemax/2:
            d=perso_joueur.vie/2
        elif fennemi.p==3 and sinatra.vie>=sinatra.viemax/2 :
            d=sinatra.vie/2
        elif david.vie>=david.viemax/2:
            d=david.vie/2
        elif  perso_joueur.vie>=perso_joueur.viemax/2:
            d=perso_joueur.vie/2
        elif sinatra.vie>=sinatra.viemax/2 and sinatra.active :
            d=sinatra.vie/2
        else:
            if random.random() <= 0.1:
                d = 150
            elif random.random() <= 0.005:
                d = 1000
            else:
                d = randint(90, 120)
        if fennemi.p == 2:
            if not david.immortal:
                if david.armure < d:
                    david.vie -= (d - david.armure)

        elif fennemi.p == 1:
            if perso_joueur.armure<d:
                perso_joueur.vie -= (d - perso_joueur.armure)

        elif fennemi.p == 3:
            if random.random() <= 0.3 + (0.05 * sinatra.ptdodge):
                sinatra.vie -= d

        affichage.affichageanimennemi(d, varanim)
        fennemi.verification()

fichier = open("quetes/mobmort", "r")
nomennemie = fichier.read()
fichier.close()
perso_joueur = perso1()
david = perso2()
sinatra = perso3()
loup = loup()
soldatpt = soldatpt()
malarich = malarich()
avalogne = avalogne()
voleur = voleur()
hornet = hornet()
goddess=goddess()
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

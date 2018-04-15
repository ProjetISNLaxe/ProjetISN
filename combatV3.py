import pygame
from pygame.locals import *
from random import *
from fennemi import *
from affichage import *
import time
from classes_tpt import *
from save import *

pygame.init()

fenetre = pygame.display.set_mode((800, 600))


def menubase(choix, c):
    if choix == 1 and c:
        attaque.menu_ = 1
        base.menu_ = 0
        c = False
    elif choix == 2 and c:
        objet.menu_ = 1
        base.menu_ = 0
        c = False
        choix = 1
    elif choix == 3 and c:
        combat.etat = "fuite"
    return choix, c


def menuobjet(choix, a, c):
    if choix == 3 and c:
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        attaque.menu_ = 0
    elif choix == 2 and soin.quantite > 0 and a == 0 and c:
        if david.ingame:
            david.vie += 50
        elif perso_joueur.ingame:
            perso_joueur.vie += 50
        elif sinatra.ingame:
            sinatra.vie += 50
        soin.quantite -= 1
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        a = 1
    elif choix == 2 and soin.quantite == 0 and a == 0 and c:
        c = False
    elif choix == 1 and resurection.quantite > 0 and a == 0 and c:
        if david.ingame:
            if sinatra.active and sinatra.vie == 0:
                sinatra.vie = 50
                sinatra.alive = True
            if perso_joueur.vie == 0:
                perso_joueur.vie = 75
                perso_joueur.alive = True
        elif perso_joueur.ingame:
            if sinatra.active and sinatra.vie == 0:
                sinatra.vie = 50
                sinatra.alive = True
            if david.vie == 0:
                david.vie = 100
                david.alive = True
        elif sinatra.ingame:
            if david.vie == 0:
                david.vie = 100
                david.alive = True
            if perso_joueur.vie == 0:
                perso_joueur.vie = 75
                perso_joueur.alive = True

        resurection.quantite -= 1
        c = False
        base.menu_ = 1
        objet.menu_ = 0
        a = 1
    elif choix == 2 and resurection.quantite == 0 and a == 0 and c:
        c = False
    return choix, a, c


def tourpartour(fenetre):  # fonction principale avec variables
    chargementsauvegarde()
    resetsauvegarde()
    action = ["attaque", "objet", "fuite", ""]
    perso_joueur.ingame=True

    armure = "cuir"
    variableanim = 0

    choix = 1  # le choix de l'action
    c = False  # la validation du choix
    d = 0

    a = 0  # une variable de validation de fin de tour

    tour = 1  # tour=1=tourperso   tour=0=tourennemi tourperso2=tour=2 etc

    pygame.key.set_repeat(200, 200)
    clock = pygame.time.Clock()
    if armure == "cuir":
        perso_joueur.armure = 2
    if armure == "chevalier":
        perso_joueur.armure = 8
    if armure == "r":
        perso_joueur.armure = 0
    if armure == "magique":
        perso_joueur.armure = 7
        perso_joueur.bonusmagique = 10

    base.menu_ = 1
    sinatra.active = False
    perso_joueur.sortdefeu=True
    adversaire = "loup"

    while combat.etat == "combatencour":  # la boucle principal
        for event in pygame.event.get():
            if event.type == QUIT:  # pour pouvoir quitter le jeux
                pygame.quit()
                exit()
            if event.type == KEYDOWN:  # les deplacements
                if event.key == K_DOWN:
                    choix += 1
                    if choix == 5:
                        choix = 1
                    if choix == 4 and (base.menu_ == 1 or objet.menu_==1 and not perso_joueur.ingame):
                        choix = 1
                if event.key == K_UP:
                    choix -= 1
                    if choix == 0:
                        if attaque.menu_ == 0:
                            choix = 3
                        else:
                            choix = 4
                if event.key == K_SPACE:
                    c = True

        if tour == 1:
            perso_joueur.ingame=True
            david.ingame=False
            sinatra.ingame=False
            if c:
                if choix == 4 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = randint(1, 5) + 10
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 3 and attaque.menu_ == 1 and c:
                    if perso_joueur.sortdefeu==True and perso_joueur.mana > 14:
                        d = 15 + perso_joueur.bonusmagique
                        perso_joueur.mana -= 15
                        a = 1
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        variableanim = 1
                    elif perso_joueur.sortdefeu==True and perso_joueur.mana < 15:
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        a = 1
                        variableanim = 2
                        perso_joueur.mana = 0
                    else:
                        c = False
                        choix = 1
                        attaque.menu_ = 0
                        base.menu_ = 1
                        a = 1
                        variableanim = 2
                        perso_joueur.mana -= 15

                if choix == 2 and attaque.menu_ == 1 and c and perso_joueur.fleche > 0:
                    d = 13
                    perso_joueur.fleche -= 1
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                    variableanim = 3

                if choix == 2 and attaque.menu_ == 1 and c and perso_joueur.fleche == 0:
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            loup.vie -= d
            if loup.vie <= 0:
                perso_joueur.xp += 50
                save()
                combat.etat = "victoire"

            if a == 1:
                affichageanim(d, tour, variableanim)
                variableanim = 0
                d = 0
                if not david.alive:
                    if sinatra.alive and sinatra.active:
                        tour = 3
                    else:
                        tour = 0
                else:
                    tour = 2
                c = False
                a = 0
            if attaque.menu_ == 1:
                if perso_joueur.sortdefeu==True:
                    action = ["l'epee", "arc", "sort de feu", "retour"]
                else:
                    action = ["l'epee", "arc", "Vous ne savez pas lancer de sort", "retour"]

            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "pôtion de mana", "retour"]

        elif tour == 2:
            perso_joueur.ingame = False
            david.ingame = True
            sinatra.ingame = False
            david.immortal = False
            if c and david.taunt == 0:
                if choix == 4 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 3 and attaque.menu_ == 1 and c:
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                    david.immortal=True
                    variableanim=5
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = randint(10, 20)
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 2 and attaque.menu_ == 1 and c:
                    david.taunt = 3
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                    variableanim = 4
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, perso, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            loup.vie -= d
            if loup.vie <= 0:
                david.xp += 50
                fermeture_plus_save()
                combat.etat = "victoire"
            if a == 1 or david.taunt > 0:
                if a == 1:
                    affichageanim(d, tour, variableanim)
                    d = 0
                if sinatra.alive and sinatra.active:
                    tour = 3
                else:
                    tour = 0
                c = False
                a = 0
                if david.taunt > 0:
                    david.taunt -= 1
            if attaque.menu_ == 1:
                action = ["tatane de faurins", "insulte", "defense", "retour"]
            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "retour", ""]

        elif tour == 3:
            perso_joueur.ingame = False
            david.ingame = False
            sinatra.ingame = True
            if c:
                if choix == 3 and attaque.menu_ == 1 and c:
                    attaque.menu_ = 0
                    base.menu_ = 1
                    choix = 1
                    c = False
                if choix == 1 and attaque.menu_ == 1 and c:
                    d = 20
                    a = 1
                    c = False
                    attaque.menu_ = 0
                    base.menu_ = 1
                if choix == 2 and attaque.menu_ == 1 and c:
                    sinatra.poison = True
                    a = 1
                    c = False
                    choix = 1
                    attaque.menu_ = 0
                    base.menu_ = 1
                if objet.menu_ == 1:
                    choix, a, c = menuobjet(choix, a, c)
                elif base.menu_ == 1:
                    choix, c = menubase(choix, c)
            loup.vie -= d
            if loup.vie <= 0:
                sinatra.xp += 50
                fermeture_plus_save()
                combat.etat = "victoire"
            if a == 1:
                affichageanim(d, tour, variableanim)
                d = 0
                tour = 0
                c = False
                a = 0
            if attaque.menu_ == 1:
                action = ["attaque furtive", "empoisonnement", "retour", ""]
            elif base.menu_ == 1:
                action = ["attaque", "objet", "fuite", ""]
            elif objet.menu_ == 1:
                action = ["resurection", "potion de soin", "retour", ""]

        elif tour == 0:
            if adversaire == "loup":
                ennemiloup()
            if not perso_joueur.alive:
                tour = 2
            elif not david.alive and sinatra.active:
                tour = 3
            else:
                tour=1
            if sinatra.poison:
                loup.vie -= 10

        if adversaire == "loup":
            enemitipe.vie = loup.vie
            enemitipe.image = loup.image

        affichage(action, tour, choix)

        if not david.alive and not perso_joueur.alive and not sinatra.alive:
            fermeture_plus_save()
            combat.etat = "mort"


        clock.tick(60)

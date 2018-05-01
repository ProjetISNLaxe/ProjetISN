import pygame as pg
import random
from Options import *
from Classes import *
from os import path

class Jeu :
    def __init__(self) :
        # initialisation de la fenêtre, etc
        pg.init()
        self.fenetre = pg.display.set_mode((LARGEUR,HAUTEUR))
        pg.display.set_caption(TITRE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self) :
        # commencer une nouvelle partie
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST :
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # boucle du jeu
        self.playing = True
        while self.playing == True :
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.display()

    def update(self):
        # boucle du jeu mise à jour
        self.all_sprites.update()
        # on vérifie si le joueur touche une plateforme (uniquement en descendant)
        if self.player.vit.y > 0 :
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top+1
                self.player.vit.y = 0
        #si le joueur arrive au 2/3 de la largeur de l'écran
        if self.player.rect.x >= LARGEUR/3 :
            self.player.pos.x -= max(abs(self.player.vit.x),2)
            for plat in self.platforms :
                plat.rect.x -= max(abs(self.player.vit.x),2)
                if plat.rect.x <= 0 :
                    plat.kill()

        #créer de nouvelles plateformes
        while len(self.platforms) < 5 :
            p = Platform(self, random.randrange(LARGEUR, LARGEUR+30),
                         random.randrange(100, HAUTEUR-30))
            self.platforms.add(p)
            self.all_sprites.add(p)

        # lorsque l'on meurt
        if self.player.rect.bottom > HAUTEUR :
            self.playing = False

    def events(self) :
        # actions / événements
        for event in pg.event.get() :
            if event.type == pg.QUIT :
                if self.playing == True :
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN :
                if event.key == pg.K_SPACE :
                    self.player.jump()

    def display(self) :
        # boucle d'affichage du jeu
        self.fenetre.fill(COULEUR_FOND)
        self.all_sprites.draw(self.fenetre)
        self.fenetre.blit(self.player.image, self.player.rect)
        self.affiche_text(str(self.score), 30, BLANC, LARGEUR-20, 20)
        # après affichage de tous les éléments, on rafraîchit l'écran
        pg.display.flip()

    def affiche_text(self, text, size, color, x, y) :
        #affiche le nombre d'ennemis tués lors de la phase 1
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.fenetre.blit(text_surface, text_rect)

    def start_screen(self):
        # écran d'accueil
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('RUNNER', 48, JAUNE, LARGEUR/2, HAUTEUR/4)
        self.affiche_text("FLECHES pour BOUGER, ESPACE pour SAUTER", 22 , JAUNE, LARGEUR/2, HAUTEUR/2)
        self.affiche_text("APPUYEZ sur une TOUCHE pour JOUER", 22 , JAUNE, LARGEUR/2, HAUTEUR*(3/4))
        pg.display.flip()
        self.wait_for_key()

    def game_over_screen(self):
        # écran lorsque l'on perd
        if self.running == False :
            return
        self.fenetre.fill(COULEUR_FOND)
        self.affiche_text('GAME OVER', 48, ROUGE, LARGEUR/2, HAUTEUR/4)
        self.affiche_text("APPUYEZ sur une TOUCHE pour REJOUER", 22 , ROUGE, LARGEUR/2, HAUTEUR/2)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting :
            self.clock.tick(FPS)
            for event in pg.event.get() :
                if event.type == pg.QUIT :
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP :
                    waiting = False

g = Jeu()
g.start_screen()
while g.running :
    g.new()
    g.game_over_screen()

pg.quit()

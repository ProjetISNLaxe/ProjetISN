import pygame
from pygame.locals import *
from sys import exit

Vx = 5
Vy = 200
vie = 3
fps = 60
noir = (0,0,0)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()
mario = pygame.image.load("mario.png").convert_alpha()
mario_jump = pygame.image.load("mario_jump.png").convert_alpha()
fond = pygame.image.load("map.jpg").convert()
mario_rect = mario.get_rect()
fond_rect = fond.get_rect()
mario_rect.x = 100
mario_rect.y = 250
pygame.key.set_repeat(10,15)
a=0

pygame.init()

while 1 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
        if event.type == KEYDOWN :
            if event.key == K_ESCAPE :
                pygame.quit()
                exit()
            if event.key == K_LEFT :
                mario_rect.x = mario_rect.x - Vx
            if event.key == K_RIGHT :
                mario_rect.x = mario_rect.x + Vx
            if event.key == K_SPACE and a==0:
                mario=mario_jump
                a=50
                mario_rect.y = mario_rect.y - Vy
    if mario_rect.y<250:
        mario_rect.y+=3
    if a>0:
        a-=1
    screen.blit(fond,fond_rect)
    screen.blit(mario,mario_rect)
    pygame.display.flip()
    clock.tick(fps)
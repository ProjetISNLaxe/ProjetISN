#!/usr/bin/python

import pygame
from pygame.locals import *
import random
import copy

pygame.init()

cBack = pygame.image.load('cards/cardback.png')
diamondA = pygame.image.load('cards/ad.png')
clubA = pygame.image.load('cards/ac.png')
heartA = pygame.image.load('cards/ah.png')
spadeA = pygame.image.load('cards/as.png')
diamond2 = pygame.image.load('cards/2d.png')
club2 = pygame.image.load('cards/2c.png')
heart2 = pygame.image.load('cards/2h.png')
spade2 = pygame.image.load('cards/2s.png')
diamond3 = pygame.image.load('cards/3d.png')
club3 = pygame.image.load('cards/3c.png')
heart3 = pygame.image.load('cards/3h.png')
spade3 = pygame.image.load('cards/3s.png')
diamond4 = pygame.image.load('cards/4d.png')
club4 = pygame.image.load('cards/4c.png')
heart4 = pygame.image.load('cards/4h.png')
spade4 = pygame.image.load('cards/4s.png')
diamond5 = pygame.image.load('cards/5d.png')
club5 = pygame.image.load('cards/5c.png')
heart5 = pygame.image.load('cards/5h.png')
spade5 = pygame.image.load('cards/5s.png')
diamond6 = pygame.image.load('cards/6d.png')
club6 = pygame.image.load('cards/6c.png')
heart6 = pygame.image.load('cards/6h.png')
spade6 = pygame.image.load('cards/6s.png')
diamond7 = pygame.image.load('cards/7d.png')
club7 = pygame.image.load('cards/7c.png')
heart7 = pygame.image.load('cards/7h.png')
spade7 = pygame.image.load('cards/7s.png')
diamond8 = pygame.image.load('cards/8d.png')
club8 = pygame.image.load('cards/8c.png')
heart8 = pygame.image.load('cards/8h.png')
spade8 = pygame.image.load('cards/8s.png')
diamond9 = pygame.image.load('cards/9d.png')
club9 = pygame.image.load('cards/9c.png')
heart9 = pygame.image.load('cards/9h.png')
spade9 = pygame.image.load('cards/9s.png')
diamond10 = pygame.image.load('cards/10d.png')
club10 = pygame.image.load('cards/10c.png')
heart10 = pygame.image.load('cards/10h.png')
spade10 = pygame.image.load('cards/10s.png')
diamondJ = pygame.image.load('cards/jd.png')
clubJ = pygame.image.load('cards/jc.png')
heartJ = pygame.image.load('cards/jh.png')
spadeJ = pygame.image.load('cards/js.png')
diamondQ = pygame.image.load('cards/qd.png')
clubQ = pygame.image.load('cards/qc.png')
heartQ = pygame.image.load('cards/qh.png')
spadeQ = pygame.image.load('cards/qs.png')
diamondK = pygame.image.load('cards/kd.png')
clubK = pygame.image.load('cards/kc.png')
heartK = pygame.image.load('cards/kh.png')
spadeK = pygame.image.load('cards/ks.png')

black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)

cards = [diamondA, clubA, heartA, spadeA,
         diamond2, club2, heart2, spade2,
         diamond3, club3, heart3, spade3,
         diamond4, club4, heart4, spade4,
         diamond5, club5, heart5, spade5,
         diamond6, club6, heart6, spade6,
         diamond7, club7, heart7, spade7,
         diamond8, club8, heart8, spade8,
         diamond9, club9, heart9, spade9,
         diamond10, club10, heart10, spade10,
         diamondJ, clubJ, heartJ, spadeJ,
         diamondQ, clubQ, heartQ, spadeQ,
         diamondK, clubK, heartK, spadeK]
cardA = [diamondA, clubA, heartA, spadeA]
card2 = [diamond2, club2, heart2, spade2]
card3 = [diamond3, club3, heart3, spade3]
card4 = [diamond4, club4, heart4, spade4]
card5 = [diamond5, club5, heart5, spade5]
card6 = [diamond6, club6, heart6, spade6]
card7 = [diamond7, club7, heart7, spade7]
card8 = [diamond8, club8, heart8, spade8]
card9 = [diamond9, club9, heart9, spade9]
card10 = [diamond10, club10, heart10, spade10,
          diamondJ, clubJ, heartJ, spadeJ,
          diamondQ, clubQ, heartQ, spadeQ,
          diamondK, clubK, heartK, spadeK]


def getAmt(card):
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        exit()


def genCard(cList, xList):
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA


def initGame(cList, uList, dList):
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA


def blackjack():
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Rejouer', 1, black)
    quitTxt = font.render('Quitter', 1, black)
    gameoverTxt = font.render('GAME OVER', 1, white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 150, 15))
    hitB = pygame.draw.rect(background, gray, (10, 445, 75, 25))
    standB = pygame.draw.rect(background, gray, (95, 445, 75, 25))
    ratioB = pygame.draw.rect(background, gray, (555, 420, 75, 50))

    while True:
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        winTxt = font.render('Wins: %i' % winNum, 1, black)
        loseTxt = font.render('Losses: %i' % loseNum, 1, black)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(
                    pygame.mouse.get_pos()):
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                stand = True
                while dealSum <= userSum and dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                restartB = pygame.draw.rect(background, (80, 150, 15), (270, 225, 75, 25))
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and quitB.collidepoint(pygame.mouse.get_pos()):
                return

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (39, 448))
        screen.blit(standTxt, (116, 448))
        screen.blit(winTxt, (565, 423))
        screen.blit(loseTxt, (565, 448))

        for card in dealCard:
            x = 10 + dealCard.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cBack, (120, 10))

        for card in userCard:
            x = 10 + userCard.index(card) * 110
            screen.blit(card, (x, 295))

        if gameover or stand:
            screen.blit(gameoverTxt, (270, 200))
            restartB = pygame.draw.rect(background, gray, (270, 225, 75, 25))
            quitB = pygame.draw.rect(background, gray, (270, 255, 75, 25))
            screen.blit(restartTxt, (287, 228))
            screen.blit(quitTxt, (287, 258))
            screen.blit(dealCard[1], (120, 10))

        pygame.display.update()

blackjack()
pygame.quit()
exit()

"""
title: brick breaker
author: Abbas Rizvi
date-created: 2023-04-24
"""

import pygame
from sprite import Sprite

import random
from text import Text
from window import Window
from player import Player
from boss import Boss
from spacers import Spacers
from background import backGround
from otherclasses.pan import Pan
from otherclasses.chicken import Chicken
from otherclasses.playerDarts import playerDarts
from otherclasses.eggcoins import eggCoins
class fryTheEgg:
    '''
    Game class for fry the egg
    '''

    def __init__(self):
        self.__WINDOW = Window("Fry The Egg")

    def run(self):
            #Window
        WINDOW = Window("Fry the Egg")

            #Background
        BACKGROUND = backGround(5, WINDOW.getWidth(), 0, 0, 0)
        BACKGROUND.setScale(0.7)

            #eggcoins
        self.__EGGCOINS = []

        for i in range(5):
            self.__EGGCOINS.append(eggCoins(10, 10, random.randrange(0, WINDOW.getWidth()), random.randrange(100, WINDOW.getHeight() - 100), 7))

            #Player
        PLAYER = Player(50,50,350,300)
        PLAYER.setScale(0.3)

            #Boss
        BOSS = Boss(50, 50, 350, 50, 20, 0)
        BOSS.setScale(0.4)

            #Frying Pan
        PAN = Pan(100, 100, 200, 200, 15)
        PAN.setScale(0.5)

        #Chicken
        CHICKEN = Chicken(50, 50, 600, 350, 3)
        CHICKEN.setScale(0.8)

        # North/South Boundaries
        SPACER1 = Spacers(5, WINDOW.getWidth(), 0, 50, 0)
        SPACER2 = Spacers(5, WINDOW.getWidth(), 0, self.__WINDOW.getHeight() - 50, 0)

        # Oil bullets list
        self.__OILDARTS = []
        # Boss position
        BOSSX = BOSS.getPOS()[0]
        BOSSY = BOSS.getPOS()[1]

        #Game over and win texts
        GameOver = Text("GAME OVER")
        GameOver.setPosition((self.__WINDOW.getWidth()//2-100, self.__WINDOW.getHeight()//2 + 100))

        YouWin = Text("YOU WIN")
        YouWin.setPosition((self.__WINDOW.getWidth() // 2 - 100, self.__WINDOW.getHeight() // 2 + 100))

        # List of oil dart objects that will be on the screen
        for i in range(5):
            self.__OILDARTS.append(
                oilDarts(10, 10, BOSSX + random.randrange(-75, 75), BOSSY + random.randrange(-75, 75), 7))


        # Player dart object
        PLAYERDARTS = playerDarts(20, 20, PLAYER.getPOS()[0], PLAYER.getPOS()[1], 15)
        PLAYERDARTS.setScale(2)

        # Health and instructions bar
        playerStats = Text((f"HP: {PLAYER.getHP()}   MOVE: WASD   FIRE: SPACE"), 36)
        playerStats.setPosition((self.__WINDOW.getWidth() // 2 - playerStats.getWidth() // 2, self.__WINDOW.getHeight() - playerStats.getHeight()))

        bossStats = Text(f"HP: {BOSS.getHP()}   TOUCH BOSS FOR MELEE ATTACK")
        bossStats.setPosition((self.__WINDOW.getWidth() // 2 - bossStats.getWidth() // 2, 0))

        MiniIns = Text((f"Collect all the eggs within 5 seconds to proceed"), 30)
        MiniIns.setPosition((self.__WINDOW.getWidth() // 2 - playerStats.getWidth() // 2,
                                     self.__WINDOW.getHeight() - playerStats.getHeight()))

        COINS = 0  # coins player collected

        while True:
            ### inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()

            # minigame blits

            WINDOW.clearScreen()
            WINDOW.getSurface().blit(BACKGROUND.getSurface(), BACKGROUND.getPOS())
            for eggcoin in self.__EGGCOINS:
                WINDOW.getSurface().blit(eggcoin.getSurface(), eggcoin.getPOS())

            #WINDOW.getSurface().blit(playerStats.getSurface(), playerStats.getPOS())

            WINDOW.getSurface().blit(PLAYER.getSurface(), PLAYER.getPOS())
            WINDOW.getSurface().blit(MiniIns.getSurface(), MiniIns.getPOS())
            WINDOW.getSurface().blit(PAN.getSurface(), PAN.getPOS())

            PRESSED_KEYS = pygame.key.get_pressed()
            PLAYER.moveWASD(PRESSED_KEYS)

            # Checking boundaries for player
            if PLAYER.getPOS()[1] > 60:
                PLAYER.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight() - 60)
            else:
                PLAYER_W = PLAYER.getPOS()[0]
                PLAYER.setPosition((PLAYER_W, 60))
                PLAYER.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight() - 60)
                print(COINS)

           # COINS = 0

            for eggcoin in self.__EGGCOINS:
                if eggcoin.isSpriteColliding(PLAYER.getPOS(), PLAYER.getDimensions()):
                    eggcoin.setPosition((10000, 10000))
                    COINS += 1
            if COINS < 5:
                if PLAYER.isSpriteColliding(PAN.getPOS(), PAN.getDimensions()):
                    print("bread")
                    PLAYER.setPosition((random.randrange(0, 800), random.randrange(50, 550)))


            if pygame.time.get_ticks() >= 5000:
                if COINS == 5:
                    MiniIns.setPosition((6000,6000))
                    BOSS.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                    BOSS.bounceX(self.__WINDOW.getWidth())

                    # Check boundaries for oil darts
                    for OILDART in self.__OILDARTS:
                        OILDART.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                        OILDART.randombounceX(800)
                        OILDART.bounceY(540)

                    # Check boundaries for chicken
                    CHICKEN.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                    CHICKEN.bounceX(800)

                    # Bliting minigame sprites on the screen

                    WINDOW.getSurface().blit(bossStats.getSurface(), bossStats.getPOS())
                    WINDOW.getSurface().blit(playerStats.getSurface(), playerStats.getPOS())
                    WINDOW.getSurface().blit(SPACER1.getSurface(), SPACER1.getPOS())
                    WINDOW.getSurface().blit(SPACER2.getSurface(), SPACER2.getPOS())


                    WINDOW.getSurface().blit(BOSS.getSurface(), BOSS.getPOS())


                    WINDOW.getSurface().blit(CHICKEN.getSurface(), CHICKEN.getPOS())

                    # Player darts movement
                    PLAYERDARTMOVE = False

                    if PLAYER.RangeAttack(PRESSED_KEYS):
                        PLAYERDARTMOVE = True

                    if PLAYERDARTMOVE == True:
                        WINDOW.getSurface().blit(PLAYERDARTS.getSurface(), PLAYERDARTS.getPOS())
                        PLAYERDARTS.checkBoundaries(self.__WINDOW.getWidth(), self.__WINDOW.getHeight())
                        PLAYERDARTS.movement(self.__WINDOW.getHeight)

                    if PLAYERDARTS.isSpriteColliding(BOSS.getPOS(), BOSS.getDimensions()):
                        BOSS._HP += -5
                        bossStats = Text((f"HP: {BOSS.getHP()}   TOUCH BOSS FOR MELEE ATTACK"))
                        bossStats.setPosition((self.__WINDOW.getWidth() // 2 - bossStats.getWidth() // 2, 0))
                        PLAYERDARTS.setPosition((PLAYER.getPOS()[0], PLAYER.getPOS()[1]))

                    if PLAYERDARTS.isSpriteColliding(SPACER1.getPOS(), SPACER1.getDimensions()) or PLAYERDARTS.getPOS()[1] < SPACER1.getPOS()[1]:
                        PLAYERDARTS.setPosition((PLAYER.getPOS()[0], PLAYER.getPOS()[1]))

                    if PLAYERDARTS.isSpriteColliding(PAN.getPOS(), PAN.getDimensions()) or PLAYERDARTS.isSpriteColliding(CHICKEN.getPOS(), CHICKEN.getDimensions()):
                        PLAYERDARTS.setPosition((PLAYER.getPOS()[0], PLAYER.getPOS()[1]))

                    # Oil darts collisions
                    for OILDART in self.__OILDARTS:
                        WINDOW.getSurface().blit(OILDART.getSurface(), OILDART.getPOS())
                        if OILDART.isSpriteColliding(PLAYER.getPOS(), PLAYER.getDimensions()) is True:
                            PLAYER._HP += -2
                            playerStats = Text((f"HP: {PLAYER.getHP()}   MOVE: WASD   FIRE: SPACE"), 36)
                            playerStats.setPosition((self.__WINDOW.getWidth() // 2 - playerStats.getWidth() // 2, self.__WINDOW.getHeight() - playerStats.getHeight()))
                            print(PLAYER.getHP())


                        if OILDART.isSpriteColliding(PAN.getPOS(), PAN.getDimensions()) or OILDART.isSpriteColliding(
                                CHICKEN.getPOS(), CHICKEN.getDimensions()):
                            OILDART.bounceX(OILDART.getHeight(), OILDART.getWidth())
                            OILDART.bounceY(OILDART.getHeight(), OILDART.getWidth())

                    # Player boss collsions
                    if PLAYER.isSpriteColliding(BOSS.getPOS(), BOSS.getDimensions()):
                        BOSS._HP += -10
                        bossStats = Text((f"HP: {BOSS.getHP()}   TOUCH BOSS FOR MELEE ATTACK"))
                        bossStats.setPosition((self.__WINDOW.getWidth() // 2 - bossStats.getWidth() // 2, 0))


                        PLAYER.randombounceXBoss(BOSS.getPOS()[0])
                        PLAYER.bounceYBoss(BOSS.getPOS()[1])
                        PLAYER.setPosition((random.randrange(0,800), random.randrange(50,550)))
                        print('hi')
                        PLAYER._HP += -1
                        playerStats = Text((f"HP: {PLAYER.getHP()}   MOVE: WASD   FIRE: SPACE"), 36)
                        playerStats.setPosition((self.__WINDOW.getWidth() // 2 - playerStats.getWidth() // 2,
                                                     self.__WINDOW.getHeight() - playerStats.getHeight()))

                    # Game over conditions
                    if PLAYER._HP <= 0:
                        #PLAYER.checkBoundaries(100000, 10000000)
                        PLAYER.setPosition((600, 200))
                        BOSS.setPosition((350, 50))
                        CHICKEN.setPosition((0, self.__WINDOW.getHeight() // 2))
                        PAN.setPosition((200, 200))
                        WINDOW.getSurface().blit(GameOver.getSurface(), GameOver.getPOS())
                        for OILDART in self.__OILDARTS:
                            OILDART.setPosition((1000 + self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))


                    elif BOSS._HP <=0:
                        PLAYER.setPosition((600, 200))
                        BOSS.setPosition((350, 50))
                        CHICKEN.setPosition((0, self.__WINDOW.getHeight() - 100 // 2))
                        PAN.setPosition((200, 200))
                        WINDOW.getSurface().blit(YouWin.getSurface(), YouWin.getPOS())
                        for OILDART in self.__OILDARTS:
                            OILDART.setPosition((1000 + self.__WINDOW.getWidth(), self.__WINDOW.getHeight()))



                        GameOver.setPosition((self.__WINDOW.getWidth() // 2 - GameOver.getWidth() // 2 - 50, self.__WINDOW.getHeight() // 2 - GameOver.getHeight() // 2))
                        #if pygame.time.get_ticks() >= 5000:
                            #pygame.quit()

                else:
                    PLAYER.setPosition((600, 200))
                    BOSS.setPosition((350, 50))
                    CHICKEN.setPosition((0, self.__WINDOW.getHeight() // 2))
                    PAN.setPosition((200, 200))
                    WINDOW.getSurface().blit(GameOver.getSurface(), GameOver.getPOS())
                    for eggcoin in self.__EGGCOINS:
                      eggcoin.setPosition((10000, 100000))

            WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = fryTheEgg()
    GAME.run()


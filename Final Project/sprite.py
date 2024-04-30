"""
title: Abstract sprite class
author: Abbas Rizvi
date-created: 2023-05-09
"""

import pygame
import random

class Sprite:
    """
    many of the common attributes and methods for sprites pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR=(0, 0, 0)):
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR #(255, 0, 255) #white
        self.__DIR_X = 1
        self.__DIR_Y = 1
        self.__random_DIR_X = random.randint(0, 1)


    # Modifier Methods
    def marqueeX(self, MAX_WIDTH, MIN_WIDTH=0):
        '''
        moves sprite
        :param MAX_WIDTH: int
        :param MIN_WIDTH: int
        :return: None
        '''
        self.__X += self.__SPD
        if self.__X > MAX_WIDTH:
            self.__X = MIN_WIDTH - self.getWidth()
        self.__POS = (self.__X, self.__Y)

    def moveWASD(self, KEYS_PRESSED):
        """
        move sprite with wasd
        :param KEYS_PRESSED: list
        :return: None
        """
        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD

        if KEYS_PRESSED[pygame.K_a]:
            self.__X -=self.__SPD

        if KEYS_PRESSED[pygame.K_w]:
            self.__Y -= self.__SPD

        if KEYS_PRESSED[pygame.K_s]:
            self.__Y += self.__SPD

        self.__POS = (self.__X, self.__Y)


    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        '''
        Check boundaries
        :param MAX_X: int
        :param MAX_Y: int
        :param MIN_X: int
        :param MIN_Y: int
        :return:
        '''
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y

        self.__POS = (self.__X, self.__Y)


    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''
        moves sprite and reverses direction horizontally
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__DIR_X = -1
        elif self.__X < SCREEN_WIDTH_MIN:
            self.__DIR_X = 1

        self._POS = (self.__X, self.__Y)

    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        '''
        moves sprite and reverses direction vertically
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_HEIGHT_MIN: int
        :return: None
        '''
        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self.__DIR_Y = -1
        elif self.__Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 1

        self._POS = (self.__X, self.__Y)

    def bounceYBoss(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        '''
        moves boss and reverses direction vertically
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_HEIGHT_MIN: int
        :return: None
        '''
        self.__Y += self.__DIR_Y * self.__SPD
        if self.__Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self.__DIR_Y = -20
        elif self.__Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 20

    def randombounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''
        moves sprite and reverses direction horizontally randomly
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        if self.__random_DIR_X == 0:
            self.__random_DIR_X = -1

        self.__X += self.__random_DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__random_DIR_X = -1
        elif self.__X < SCREEN_WIDTH_MIN:
            self.__random_DIR_X = 1

        self._POS = (self.__X, self.__Y)

    def randombounceXBoss(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''
        moves boss and reverses direction horizontally randomly
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        #   if self.__DIR_X != 1 or -1:
        # self.__DIR_X = random.randint(0, 1)
        if self.__random_DIR_X == 0:
            self.__random_DIR_X = -20

        self.__X += self.__random_DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__random_DIR_X = -20
        elif self.__X < SCREEN_WIDTH_MIN:
            self.__random_DIR_X = 20

        self._POS = (self.__X, self.__Y)

    def movement(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        '''
        moves sprite
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_HEIGHT_MIN: int
        :return: None
        '''
        self.__Y += -self.__SPD

    def setWidth(self, WIDTH):
        '''
        sets width of sprite
        :param WIDTH: int
        :return: None
        '''
        self.__WIDTH = WIDTH
        self.__DIM = (self.__WIDTH, self.__HEIGHT)

    def setHeight(self, HEIGHT):
        '''
        sets height of sprite
        :param HEIGHT: int
        :return: None
        '''
        self.__HEIGHT = HEIGHT
        self.__DIM = (self.__WIDTH, self.__HEIGHT)

    def setPosition(self, TUPLE):
        '''
        sets sprites position on screen
        :param TUPLE: list
        :return: None
        '''
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)

    def setColor(self, TUPLE):
        '''
        Sets sprite's color
        :param TUPLE: list
        :return: None
        '''
        self._COLOR = TUPLE

    def setSpeed(self, SPD):
        '''
        set the speed sprite moves
        :param SPD: int
        :return: None
        '''
        self.__SPD = SPD

    # Accessor Methods
    def getWidth(self):
        '''
        get's the width of sprite
        :return: int
        '''
        return self._SURFACE.get_width()

    def getHeight(self):
        '''
        gets the height of sprite
        :return: int
        '''
        return self._SURFACE.get_height()

    def getDimensions(self):
        '''
        gets the dimensions of the sprite
        :return: list
        '''
        return (self._SURFACE.get_width(), self._SURFACE.get_height())

    def getPOS(self):
        '''
        gets the position of the sprite
        :return: list
        '''
        return self.__POS

    def getSurface(self):
        '''
        gets the surface of the sprite
        :return: obj
        '''
        return self._SURFACE

    def isSpriteColliding(self, POSITION, DIMENSION):
        """
        Check if a sprite is colliding with the current sprite
        :param POSITION: tuple
        :param DIMENSION: tuple
        :return: bool
        """
        SPRITE_X = POSITION[0]
        SPRITE_Y = POSITION[1]
        SPRITE_W = DIMENSION[0]
        SPRITE_H = DIMENSION[1]

        if SPRITE_X >= self.__X - SPRITE_W and SPRITE_X <= self.__X + self.getWidth():
            if SPRITE_Y >= self.__Y - SPRITE_H and SPRITE_Y <= self.__Y + self.getHeight():
                return True

        return False


    def setScale(self, SCALE_X, SCALE_Y = 0):
        """
        Resize the image based on a factor
        :param SCALE_X: float
        :param SCALE_Y: float
        :return: None
        """
        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()* SCALE_Y))





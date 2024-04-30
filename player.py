#player.py

'''
title: Player Class
author: Abbas Rizvi
date: 2023/05/10
'''
from sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 10):
        '''
        Box constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/player.png")
        self._SCORE = 0
        self._HP = 40
        self._MEELE_ATT = 20
        self._RANGE_ATT = 10


    def moveWASD(self, KEYS_PRESSED):
        '''
        player movement
        :param KEYS_PRESSED: string
        :return: none
        '''
        Sprite.moveWASD(self, KEYS_PRESSED)

    def checkBoundaries(self, MAX_X, MAX_Y):
        '''
        keeps player on screen
        :param MAX_X: list
        :param MAX_Y: list
        :return: None
        '''
        Sprite.checkBoundaries(self, MAX_X, MAX_Y)

    def CloseAttack(self, KEYS_PRESSED):
        '''
        returns player's close range attack
        :param KEYS_PRESSED: string
        :return: boolean
        '''
        if KEYS_PRESSED[pygame.K_r]:
            return True

    def RangeAttack(self, KEYS_PRESSED):
        '''
        returns player's long range attack
       :param KEYS_PRESSED: string
       :return: boolean
       '''
        if KEYS_PRESSED[pygame.K_SPACE]:
            return True

    def getHP(self):
        '''
        get's the players current hp
        :return: float
        '''
        return self._HP


'''
title: background sprite
author: Abbas Rizvi
date: 2023/06/01
'''
from sprite import Sprite
import pygame

class backGround(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 10):
        '''
        background constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/grill.jpg")
        self._SCORE = 0
        # self._HP = 20
        self._MEELE_ATT = 20
        self._RANGE_ATT = 10

    def checkBoundaries(self, MAX_X, MAX_Y):
        '''
        checks if player is out of scree
        :param MAX_X: int
        :param MAX_Y: int
        :return: None
        '''
        Sprite.checkBoundaries(self, MAX_X, MAX_Y)

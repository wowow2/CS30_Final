'''
title: egg
author: Abbas Rizvi
date: 2023/06/02
'''
from sprite import Sprite
import pygame

class eggCoins(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 10):
        '''
        pan sprite constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/eggcoin.png")
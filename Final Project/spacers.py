'''
title: Spacers
author: Abbas Rizvi
date: 2023/05/31
'''
from sprite import Sprite
import pygame

class Spacers(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 10):
        '''
        spacers for text constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)
        self._SCORE = 0

        self._MEELE_ATT = 20
        self._RANGE_ATT = 10



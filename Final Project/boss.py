#boss.py

'''
title: Egg Class
author: Abbas Rizvi
date: 2023/05/10
'''

from sprite import Sprite
from otherclasses.oildarts import oilDarts
import pygame

class Boss(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 15, TIME=0):
        '''
        Box constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32) #(self._DIM, pygame.SRCALPHA, pygame.image.load("images/boss.png")) #(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/boss.png")
        self._HP = 200
        self._MEELE_ATT = 30
        self._RANGE_ATT = 10
        self._TIME = TIME

    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''

        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        Sprite.bounceX(self, SCREEN_WIDTH_MAX)

    def getHP(self):
        '''
        :return: player HP
        '''
        return self._HP






'''
title: Oil Darts thrown by player and egg
author: Abbas Rizvi
date: 2023/05/12
'''
from sprite import Sprite
import pygame
import random

class oilDarts(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 0):
        '''
        oildart sprite constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/oildart.png")

    def randombounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''
        moves dart horizontally and bounces it randomly
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        Sprite.randombounceX(self, SCREEN_WIDTH_MAX)

    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=60):
        '''
        moves dart vertically and bounces it
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_HEIGHT_MIN: int
        :return: None
        '''
        Sprite.bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN)

    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        '''
        moves dart horizontally and bounces it
        :param SCREEN_WIDTH_MAX: int
        :param SCREEN_WIDTH_MIN: int
        :return: None
        '''
        Sprite.bounceX(self, SCREEN_WIDTH_MAX)



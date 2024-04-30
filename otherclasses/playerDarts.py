'''
title: Oil Darts thrown by player and egg
author: Abbas Rizvi
date: 2023/05/12
'''
from sprite import Sprite
import pygame
import random

class playerDarts(Sprite):
    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPD = 5):
        '''
        player oil dart constructor
        :param WIDTH: int
        :param HEIGHT: int
        :param X: float
        :param Y: float
        '''
        Sprite.__init__(self, WIDTH, HEIGHT, X, Y, SPD)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE = pygame.image.load("images/oildart.png")

    def movement(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        '''
        moves player dart upwards only
        :param SCREEN_HEIGHT_MAX: int
        :param SCREEN_HEIGHT_MIN: int
        :return: None
        '''
        Sprite.movement(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN)





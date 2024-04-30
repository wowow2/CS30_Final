#text.py
'''
title: Text class
author: Abbas Rizvi
date-created: 2023/05/10
'''

import pygame
from sprite import Sprite
class Text(Sprite):
    '''
    Create's text as a sprite
    '''
    def __init__(self, TEXT, FONT_SIZE=36):
        Sprite.__init__(self)
        self.__TEXT = TEXT
        self.__FONT_SIZE = FONT_SIZE
        self.__FONT = pygame.font.SysFont("Comic Sans", self.__FONT_SIZE) # Secular One?
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setColor(self, TUPLE):
        '''
        sets the color of the sprite
        :param TUPLE: list
        :return: None
        '''
        Sprite.setColor(self,TUPLE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)

    def setFontSize(self, NEW_SIZE):
        '''
        set's the size of the sprite/text
        :param NEW_SIZE: int
        :return: None
        '''
        self.__FONT_SIZE = NEW_SIZE
        self.__FONT = pygame.font.SysFont("Comic Sans", self.__FONT_SIZE)
        self._SURFACE = self.__FONT.render(self.__TEXT, True, self._COLOR)


"""
title: window
author: Abbas Rizvi
date-created: 2023-05-09
"""

import pygame

class Window:
    """
    Create the window that will load the game
    :return: None
    """
    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE # text that appears in the title bar
        self.__FPS = FPS # the frames/second the window will refresh
        info = pygame.display.Info()
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        #self.__WIDTH = info.current_w
        #self.__HEIGHT = info.current_h
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__BG_COLOR = (128, 128, 128) # uses the format (R, G, B)
        self.__FRAME = pygame.time.Clock()

        self._SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)

    # MODIFIER METHODS
    def updateFrame(self):
        """
        Update the Window object based on the FPS
        :param self:
        :return:
        """
        self.__FRAME.tick(self.__FPS) # Waits for the appropriate time based on the set FPS
        pygame.display.flip() # Updates the window with the new frame.

    def clearScreen(self):
        """
        Fill the screen with the back color
        :return:
        """
        self._SURFACE.fill(self.__BG_COLOR)


    # ACCESSOR METHODS
    def getSurface(self):
        '''
        gets the surface of the window
        :return: obj
        '''
        return self._SURFACE

    def getWidth(self):
        '''
        gets the width of the window
        :return: int
        '''
        return self.__WIDTH #.get_width()

    def getHeight(self):
        '''
        gets the height of the window
        :return: int
        '''
        return self.__HEIGHT #.get_height()

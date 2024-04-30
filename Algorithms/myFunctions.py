#myFunctions.py

"""
title: Common Functions for all sort algorithms
author: Abbas Rizvi
date created: Feb 3rd, 2023
"""

import random, time, statistics

def getSmallList():
    """
    returns a small list of mixed integers
    :return: LIST
    """

    return [5,1,19,1,11,17,7,13]

def getList(SIZE):
    """
    return a sortd list of approximately size SIZE
    :param SIZE: int
    :return: list
    """
    NUMBERS = []
    for i in range(2*SIZE):
        if random.randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def getRandomList(SIZE):
    """
    returns a randomized list of approximately size SIZE
    :param SIZE: (int)
    :return: list (int)
    """
    SORTED_LIST = getList(SIZE)
    RANDOM_LIST = []

    for i in range(len(SORTED_LIST)):
        RANDOM_LIST.append(SORTED_LIST.pop(random.randrange(len(SORTED_LIST))))

    return RANDOM_LIST

def getAverage(TIMES):
    """
    Returns the average of the given list
    :param TIMES: list (float)
    :return: (float)
    """

    return statistics.mean(TIMES)

def getTime():
    """
    Returns the performance counter
    :return: (float)
    """
    return time.perf_counter()
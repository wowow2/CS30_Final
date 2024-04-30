# b_binary_search.py

"""
author: Abbas Rizvi
title: Bineary Search
Date: Febuary 2nd, 2023
"""

from random import randrange
from time import perf_counter
from statistics import mean
def createArray(SIZE=20000):
    '''
    Create an ordered list of random numbers
    :param SIZE: int
    :return: LIST (int)
    '''

    NUMBERS = []
    for i in range(SIZE):
        if randrange(2) == 1:
            NUMBERS.append(i)
    return NUMBERS

def binarySearch(LIST, VALUE):
    '''
    Search for a Value within a list
    :param LIST: LIST (int)
    :param VALUE: int
    :return: bool
    '''

    SMALL_IND = 0
    LARGE_IND = len(LIST)-1

    while SMALL_IND < LARGE_IND:
        MIDPOINT_IND = (SMALL_IND + LARGE_IND) // 2
        if LIST[MIDPOINT_IND] == VALUE:
            return True
        elif VALUE > LIST[MIDPOINT_IND]:
            SMALL_IND = MIDPOINT_IND + 1
        else:
            LARGE_IND = MIDPOINT_IND
    return False

if __name__ == "__main__":
    NUMBERS = createArray(1000000)

    TIMES = []

    for i in range(30):
        NUMBER = NUMBERS[randrange(len(NUMBERS))]

        START = perf_counter()
        print(binarySearch(NUMBERS, NUMBER))
        END = perf_counter()

        TIMES.append(END - START)
    print(mean(TIMES))
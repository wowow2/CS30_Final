# j_quicksort.py

"""
title: Quick Sort
Author: Abbas Rizvi
Date: 2023/02/14
"""

from myFunctions import *

def quicksort(LIST, FIRST_INDEX, LAST_INDEX):
    """
    quicksort
    :param LIST: list(int)
    :param FIRST_INDEX: int
    :param LAST_INDEX: int
    :return: None
    """
    if FIRST_INDEX < LAST_INDEX:
        PIVOT_VALUE = LIST[FIRST_INDEX]
        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False
        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                LEFT_INDEX += 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE:
                RIGHT_INDEX -= 1

            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True
            else:
                TEMP = LIST[LEFT_INDEX]
                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]
                LIST[RIGHT_INDEX] = TEMP
        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP

        quicksort(LIST, FIRST_INDEX, RIGHT_INDEX-1)
        quicksort(LIST, RIGHT_INDEX+1, LAST_INDEX)

if __name__ == "__main__":

    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        quicksort(NUMBERS, 0, len(NUMBERS) -1)
        END = getTime()
        TIMES.append(END - START)
    print(f"Average:{getAverage(TIMES)} seconds")

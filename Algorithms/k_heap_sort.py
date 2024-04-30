# k_heap_sort

"""
title: Heap Sort
author: Abbas Rizvi
date-created: 2023/02/16
"""

from myFunctions import *

def heapify(LIST, LEN_ARRAY, ROOT_INDEX):
    """
    Heapifies all subtrees in the binary tree
    :param LIST: list(int)
    :param LEN_ARRAY: int - length of array
    :param ROOT_INDEX: int - Parent index
    :return: None
    """

    LARGEST_INDEX = ROOT_INDEX #Assuming root index is the highest
    LEFT_INDEX = 2 * ROOT_INDEX + 1
    RIGHT_INDEX = 2 * ROOT_INDEX + 2

    if LEFT_INDEX < LEN_ARRAY and LIST[ROOT_INDEX] < LIST[LEFT_INDEX]:
        LARGEST_INDEX = LEFT_INDEX

    if RIGHT_INDEX < LEN_ARRAY and LIST[LARGEST_INDEX] < LIST[RIGHT_INDEX]:
        LARGEST_INDEX = RIGHT_INDEX

    if LARGEST_INDEX != ROOT_INDEX:
        TEMP = LIST[ROOT_INDEX]
        LIST[ROOT_INDEX] = LIST[LARGEST_INDEX]
        LIST[LARGEST_INDEX] = TEMP

        # heapify the root
        heapify(LIST, LEN_ARRAY, LARGEST_INDEX)

def heap_sort(LIST):
    """
    Sorts the list
    :param LIST: list(int)
    :return: None
    """

    LEN_ARRAY = len(LIST)

    # build a max heap
    for i in range(LEN_ARRAY-1, -1, -1):
        heapify(LIST, LEN_ARRAY, i)

    # Extract the highest value in the heap and recur

    for i in range(LEN_ARRAY-1, 0, -1):
        LIST[i], LIST[0] = LIST[0], LIST[i]

        heapify(LIST, i, 0)


if __name__ == "__main__":

    #NUMBERS = getSmallList()
    #heap_sort(NUMBERS)
    #print(NUMBERS)

    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        heap_sort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(TIMES[-1])
    print(f"Average:{getAverage(TIMES)} seconds")
# i_merge_sort.py

"""
title: Merge Sort
author: Abbas Rizvi
date: 2023/02/13
"""

from myFunctions import *

def mergeSortedList(LEFT_LIST, RIGHT_LIST):
    """
    Iterative merge of two sorted lists
    :param LEFT_LIST: list(int)
    :param RIGHT_LIST: list(int)
    :return: list(int)
    """

    #Special Case: One or both lists are empty
    if len(LEFT_LIST) == 0:
        return RIGHT_LIST
    elif len(RIGHT_LIST) == 0:
        return LEFT_LIST

    #General Case
    INDEX_LEFT = 0
    INDEX_RIGHT = 0
    LIST_MERGED = []
    LIST_LEN_TOTAL = len(LEFT_LIST) + len(RIGHT_LIST)

    while len(LIST_MERGED) < LIST_LEN_TOTAL:
        if LEFT_LIST[INDEX_LEFT] <= RIGHT_LIST[INDEX_RIGHT]:
            LEFT_LIST.append(LEFT_LIST[INDEX_LEFT])
            INDEX_LEFT = INDEX_LEFT + 1
        else:
            LIST_MERGED.append(RIGHT_LIST[INDEX_RIGHT])
            INDEX_RIGHT += 1

        # test if we are at the end of one of the lists
        if INDEX_RIGHT == len(RIGHT_LIST):
            LIST_MERGED = LIST_MERGED + LEFT_LIST[INDEX_LEFT:]
            break
        elif INDEX_LEFT == len(LEFT_LIST):
            LIST_MERGED += RIGHT_LIST[INDEX_RIGHT]

    return LIST_MERGED

def mergeSort(LIST):
    """
    Revursive Split of the merge Sort
    :param LIST: (int)
    :return: (LIST)
    """

    if len(LIST) <= 1:
        # base case
        return LIST
    else:
        MIDPOINT = len(LIST) // 2
        LEFT = LIST[:MIDPOINT]
        RIGHT = LIST[MIDPOINT:]

        return mergeSortedList(mergeSort(LEFT), mergeSort(RIGHT))


if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        SORTED_NUMBERS = mergeSort(NUMBERS)
        END = getTime()
        TIMES.append(END-START)
        print(TIMES[-1])

    print(getAverage(TIMES))
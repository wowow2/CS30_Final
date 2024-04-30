# e_insertion_sort.py

"""
title: Inserstion Sort Algorithm
Author: Abbas Rizvi
date-created: Feb 8th, 2023
"""

from myFunctions import *

def insertSort(LIST):
    """
    takes the lowest value in the unsorted half of the list and inserts it into the relative position within
    the sorted list.
    :param LIST: list (int)
    :return: None
    """
    for i in range(1, len(LIST)):
        INDEX_VALUE = LIST[i] # Saving the VALUE of the lowest index in the unsorted section of the list
        SORTED_INDEX = i - 1 # Identify the largest index of the sorted section of the list

        while SORTED_INDEX >=0 and INDEX_VALUE < LIST[SORTED_INDEX]:
            # while traversing tail-to-head in the sorted section.
            LIST[SORTED_INDEX +1] = LIST[SORTED_INDEX] # overwrite the right value
            SORTED_INDEX = SORTED_INDEX - 1 # move one to the left
            # STOP when SORTED_INDEX reaches 0 or the LIST[SORTED_INDEX] is smaller than the index value

        LIST[SORTED_INDEX + 1] = INDEX_VALUE # Replace the SORTED INDEX position with INDEX VALUE
            # NOTE: One is added to the SORTED_INDEX to adjust for the minus one at the end of while loop


if __name__ == "__main__":

    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        insertSort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(TIMES[-1])
    print(f"Average:{getAverage(TIMES)} seconds")
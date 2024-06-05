# e_insertion_sort.py

"""
title: Insertion Sort Algorithm
Author: Abbas Rizvi
date-created: Feb 8th, 2023
"""

from myFunctions import *

def insert_sort(list_):
    """
    takes the lowest value in the unsorted half of the list and inserts it into the relative position within
    the sorted list.
    :param list_: list (int)
    :return: None
    """
    for i in range(1, len(list_)):
        index_value = list_[i] # Saving the VALUE of the lowest index in the unsorted section of the list
        sorted_index = i - 1 # Identify the largest index of the sorted section of the list

        while sorted_index >=0 and index_value < list_[sorted_index]:
            # while traversing tail-to-head in the sorted section.
            list_[sorted_index + 1] = list_[sorted_index] # overwrite the right value
            sorted_index = sorted_index - 1 # move one to the left
            # STOP when sorted_index reaches 0 or the list_[sorted_index] is smaller than the index value

        list_[sorted_index + 1] = index_value # Replace the sorted_index position with index_value
            # NOTE: One is added to the sorted_index to adjust for the minus one at the end of while loop


if __name__ == "__main__":

    times = []
    for i in range(30):
        numbers = getRandomList(10000)
        start = getTime()
        insert_sort(numbers)
        end = getTime()
        times.append(end - start)
        print(times[-1])
    print(f"Average:{getAverage(times)} seconds")

# j_quicksort.py

"""
title: Quick Sort
Author: Abbas Rizvi
Date: 2023/02/14
"""

from myFunctions import *

def quicksort(list_, first_index, last_index):
    """
    quicksort
    :param list_: list(int)
    :param first_index: int
    :param last_index: int
    :return: None
    """
    if first_index < last_index:
        pivot_value = list_[first_index]
        left_index = first_index + 1
        right_index = last_index

        done = False
        while not done:
            while left_index <= right_index and list_[left_index] <= pivot_value:
                left_index += 1
            while right_index >= left_index and list_[right_index] >= pivot_value:
                right_index -= 1

            if right_index < left_index:
                done = True
            else:
                temp = list_[left_index]
                list_[left_index] = list_[right_index]
                list_[right_index] = temp
        temp = list_[first_index]
        list_[first_index] = list_[right_index]
        list_[right_index] = temp

        quicksort(list_, first_index, right_index-1)
        quicksort(list_, right_index+1, last_index)

if __name__ == "__main__":
    '''
    times = []
    for i in range(30):
        numbers = getRandomList(10000)
        start = getTime()
        quicksort(numbers, 0, len(numbers) -1)
        end = getTime()
        times.append(end - start)
    print(f"Average:{getAverage(times)} seconds")
    '''

    list = [5,3,7,1,6]
    quicksort(list, 0, len(list) - 1)
    print(list)
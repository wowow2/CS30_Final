# k_heap_sort

"""
title: Heap Sort
author: Abbas Rizvi
date-created: 2023/02/16
"""

from myFunctions import *

def heapify(lst, len_array, root_index):
    """
    Ensures the subtree rooted at root_index follows the max-heap property.
    :param lst: list(int) - The list to be heapified
    :param len_array: int - The length of the array
    :param root_index: int - The root index of the subtree to heapify
    :return: None
    """

    # Initialize largest as root
    largest_index = root_index
    # Left child index calculation
    left_index = 2 * root_index + 1
    # Right child index calculation
    right_index = 2 * root_index + 2

    # Check if left child exists and is greater than root
    if left_index < len_array and lst[root_index] < lst[left_index]:
        largest_index = left_index

    # Check if right child exists and is greater than the current largest
    if right_index < len_array and lst[largest_index] < lst[right_index]:
        largest_index = right_index

    # If the largest element is not the root, swap and continue heapifying
    if largest_index != root_index:
        # Swap root and largest
        lst[root_index], lst[largest_index] = lst[largest_index], lst[root_index]

        # Recursively heapify the affected subtree
        heapify(lst, len_array, largest_index)

def heap_sort(lst):
    """
    Sorts a list in ascending order using the heap sort algorithm.
    :param lst: list(int) - The list to be sorted
    :return: None
    """

    len_array = len(lst)

    # Build a max-heap: reorganize the list into a heap
    # Start from the last non-leaf node and heapify each node
    for i in range(len_array // 2 - 1, -1, -1):
        heapify(lst, len_array, i)

    # One by one extract elements from the heap
    for i in range(len_array - 1, 0, -1):
        # Move current root (largest) to the end
        lst[i], lst[0] = lst[0], lst[i]

        # Call heapify on the reduced heap
        heapify(lst, i, 0)




if __name__ == "__main__":

    #NUMBERS = getSmallList()
    #heap_sort(NUMBERS)
    #print(NUMBERS)
    '''
    TIMES = []
    for i in range(30):
        NUMBERS = getRandomList(10000)
        START = getTime()
        heap_sort(NUMBERS)
        END = getTime()
        TIMES.append(END - START)
        print(TIMES[-1])
    print(f"Average:{getAverage(TIMES)} seconds")
    '''
    list = [5, 3, 7, 1, 6]
    heap_sort(list)
    print(list)
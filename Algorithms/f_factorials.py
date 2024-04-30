# f_factorials.py
'''
title: Factorials with recursion
author: Abbas Rizvi
date-created: February 9th, 2023
'''

def recursiveFactorials(NUMBER):
    """
    calculates the factorial of a given number
    :param NUMBER: (int)
    :return: (int)
    """
    if NUMBER == 0:
        # base case
        return 1
    else:
        return NUMBER * recursiveFactorials(NUMBER - 1)

def iterativeFactorial(NUMBER):
    """
    Iteratively calculates the factorial of a number
    :param NUMBER: (int)
    :return: (int)
    """
    NUM = 1
    for i in range(1, NUMBER + 1):
        NUM *= 1
    return NUM


if __name__ == "__main__":
    NUM = int(input("Enter a Number: "))

    if NUM < 0:
        print("Sorry factorials, don't exist for negative numbers.")
    else:
        FACTORIAL = iterativeFactorial(NUM)
        print(f"The Factorial of {NUM} is {FACTORIAL}.")
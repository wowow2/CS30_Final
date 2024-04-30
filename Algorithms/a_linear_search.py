# a_linear_search.py

"""
title: Linear Search
Date: Febuary 2nd, 2023
Author: Abbas Rizvi
"""
import random
import time
import statistics
# Make a large dataset
NUMBERS = []
for i in range(2000000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)

# Storing Times
TIMES = []

for i in range(30):
    # Pick a Number
    NUMBER = NUMBERS[random.randrange(len(NUMBERS))]
    # Search for the VALUE
    START_TIME = time.perf_counter()
    for i in range(len(NUMBERS)):
        if NUMBERS[i] == NUMBER:
            print("Found!")
            break  # Stops the for loop
    END_TIME = time.perf_counter()
    TIMES.append(END_TIME - START_TIME)

print(statistics.mean(TIMES))


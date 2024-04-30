# c_bubble_sort.py

"""
 title: bubble sort
 date-created: Feb 3rd, 2023
 author: Abbas Rizvi
"""
import myFunctions
def bubbleSort(LIST):
     """
     Compares two adjacent values and moves the highest one to the end of the list.
     :param LIST:
     :return: None
     """

     for i in range(len(LIST)-1,0,-1): # traverses backwards from end to index 1
        for j in range(i): # traverses forward in the unsorted section
            # check to switch two current values
             if LIST[j] > LIST[j+1]:
                 TEMP = LIST[j]
                 LIST[j] = LIST[j+1]
                 LIST[j+1] = TEMP
                 # LIST[j], LIST[j+1] = LIST[j+1], LIST[j]

if __name__ == "__main__":
    TIMES = []
    for i in range(30):
        NUMBERS = myFunctions.getRandomList(10000)
        START = myFunctions.getTime()
        bubbleSort(NUMBERS)
        END = myFunctions.getTime()
        TIMES.append(END-START)
        print(END-START)

    print(f"Average {myFunctions.getAverage(TIMES)} s")
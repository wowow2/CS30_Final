# notes.md

# CSE3110 - Iterative Algorithms

Iterative algorithms are algorithms that use loops to process large sets of data. This includes while loops and for loops. In contrast, Recursive algorithms are algorithms that call the same algorithms over and over again to process large sets of data. Iterative algorithms tend to be easier to design, but may increase in efficiency when using recursive algorithms.

Iterative algorithms are easily shown in search and sort algorithms. 

## Linear Search

Linear Search is the easier program, but least efficient method of search. It processes the data line-by-line, similar to brute force decryption algorithms when cracking passwords. 

```python
FOUND = False
for i in range(len(LIST)):
    if VALUE == LIST[i]:
        FOUND = True
        break
```

Linear Search processing time is dependent on the length of the array and the value's placement in the array. Arrays that are 10000 indices or higher can have a noticeable time requirement to process. 

#### Measuring Time
To measure processing time, the ```time.perf_counter()``` will measure the approximate milliseconds it takes to run the program

For more accurate results, we use the average of at least 30 trials and then use ```statistics.mean()``` to find the average

## Binary Search
Binary search follows the _divide and conquer_ technique of finding a value. It takes an __ordered__ set of data and tests the midpoint. Then it cuts the list in half and reruns the process.

__Steps for binary search__
1. Determine the midpoint of the search
2. Test if the midpoint is the found value
   1. If the midpoint is the found value, end.
   2. If the midpoint is larger than the midpoint, redefine the lowest value of the list to be the midpoint.
   3. if the value is smaller than the midpoint, redefine the largest value of the to be one below the midpoint
3. Repeat until the value is found. 

* Advantages of Binary Search
   * It is significantly faster than linear search
* Disadvantages of Binary Search
   * List must be sorted from smallest to largest
   * List must only contain integers or floats
   * Harder to program

## Sorting Data
Just like searching algorithms, sorting alogrithms have varying levels of efficiency. There are several types of sort alogrithms including bubble, selection, insertion, and merge. Python uses Timsort, which is a hybrid of merge and insertion sort designed by Tim Peters in 2002.

### Bubble Sort
Bubble sort compares low adjacent values on the list and arranges them from lowest to highest. Then it moves to the next index pair and repeats until it reaches the end of the unsorted list. The final index is the value that is sorted and the algorithm repeats until each index (traversed tail to head) is sorted.

Note: Sort algorithms separate the list into a sorted and unsorted section when referencing the progression of the sort algorithm. With each iteration of the sort, one value in the unsorted section is placed into the sorted section.

Advantages of bubble sort include that it is relatively easy to program and takes less memory; the disadvantages include long processing time directly proportional to the length of the data set. However, the set is often fully sorted before the last iteration. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---|---|---|---|---|---|---|---|
| 1 | 3 | 5 | 11 | 17 | 7 | 13 | __19__ |
| 1 | 3 | 5 | 11 | 7 | 13 | __17__ | 19 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 17 | 19 |
| 1 | 3 | 5 | 7 | __11__ | 13 | 17 | 19 |
| 1 | 3 | 5 | __7__ | 11 | 13 | 17 | 19 |
| 1 | 3 | __5__ | 7 | 11 | 13 | 17 | 19 |
| 1 | __3__ | 5 | 7 | 11 | 13 | 17 | 19 |

NOTE: For the unit exam you might be asked information from a specific iteration of an algorithm.

### Selection Sort
Selection sort compares the current index value with the rest of the set. It will find the lowest value and switch positions with the lowest index position of unsorted half of the list. As it runs through the data set, it will select the lowest value and place it in the lowest position on the unsorted section of the list.

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---|---|---|---|---|---|---|---|
| __*1*__ | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | __*11*__ | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | 11 | __13__ | 19 | _17_ |
| 1 | 3 | 5 | 7 | 11 | 13 | __17__ | _19_ |


### Insertion Sort
Insertion sort splits the list into two sections: sorted and unsorted. As it progresses through the list it takes the value at the lowest index of the unsorted half and inserts it into the correct _relative_ location in the sorted section of the list. The list is only fully sorted, where all values are in the appropriate index location after the final iteration. 

| 1 | 5 | 3 | 19 | 11 | 17 | 7 | 13 |
|---|---|---|---|---|---|---|---|
| 1 | __*5*__ | 3 | 19 | 11 | 17 | 7 | 13 |
| 1 | __3__ | _5_ | 19 | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __*19*__ | 11 | 17 | 7 | 13 |
| 1 | 3 | 5 | __11__ | _19_ | 17 | 7 | 13 |
| 1 | 3 | 5 | 11 | __17__ | _19_ | 7 | 13 |
| 1 | 3 | 5 | __7__ | 11 | 17 | _19_ | 13 |
| 1 | 3 | 5 | 7 | 11 | _13_ | 17 | 19 |

# CSE3310 - Recursive algorithms
A __recursive algorithm__ calls itself with smaller or simpler input values. Recursive algorithms rely on _base case_, which is the simplest input value. Then there are subprocesses that simplifies more complex input values and returns the simplified values to the _same function_.

NOTE: All iterative algorithms can be written recursively and vice versa, however, certian functions are eaiser to write in one form over another.

## Example 1: Testing for correct input
```python
# iterative
def checkInt(NUMBER):
    while True:
        if NUMBER.isnumeric():
            return int(NUMBER)
        else:
            print("You did not enter a number")
            NUMBER = input("Please enter a number: ")

# recursive
def checkInt(NUMBER):
    if NUMBER.isnumeric():
        return int(NUMBER) # BASE CASE
    else:
        # SUBPROCESS TO SIMPLIFY THE INPUT VALUE
        print("You did not enter a number")
        return checkInt(input("Please enter a number: "))   
```

## Iteration vs Recursion 
In general. Iterative algorithms require more lines of code and more variables than recursive alogrithms. It relies on while and for loops to complete the process. Onen iteration of an iterative algorithm is one loop through the while or for loop. There as recursive algorithms do not use as many variables or loop because return values are re-entered into a _new instance_ of the same function. Therefore, recursions requires more physical memory than iterative algorithms because each instance of the recursive function stays in memory until the base case is achieved. In recursion one instance of the function is one iteration of the recursive function. 

## Example 2: Factorials
###  Calculate 7!
7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 * 1

but!
6! = 6 * 5 * 4 * 3 * 2 * 1

thus!
7! = 7 x 6!

Continuing the pattern,
Our base case is 1! because each factorial could be broken down

Therefore, we can generalize factorials as,
```
f(x) = x * f(x-1), x > 1 --> Subprocess to simplify the input
     = 1, x = 1 --> base case
```

## Sorting
Recursive sorting uses both recursive and iterative processes in the algorithm. (Algorithms use for/while loops and return the function or a sub function). In general, these hybrid sorts are exponentially faster with longer lists. (They are measured on a logarithmic scale).

### Merge Sort
Merge sort follows a divide and conquer method of sorting, where the array is split into its base length and then rebuilds the list by combining progressively larger sorted lists togather. The recursive portion is the splitting of the list and iterative portion is the actual merging of the two smaller sorted lists togather.

Often this function is separated into splitting and merging functions.

### Quick Sort
Quick sort (quicksort) is another divide and conquer method of sorting. Quicksort uses an arbitrary value as its pivot, which is then used to place the pivot in the correct place in the array. It does this by placing all smaller values to the left of the pivot and all larger values to the right of the pivot. Then it places pivot value where smaller and larger portions intersect. Then it moves to the next pivot value, recurring until a sublist is a length of one.

NOTE: Quick sort's efficiency is from separating the list into two sections that will never compare values with each other again.

### Heap Sort
Heap sort uses a binary tree organization of an array to sort higher values to the tip of tree (lower indexes of the array). Notes that while this algorithm represents the numbers in a binary tree, they are still stored in an array. The process of moving larger values higher in the binary tree is called __heapifying__.

To build a binary tree, each index (starting at 0), will have a left child and a right child. The index values can be calculated from the following

```
left_child_index = 2 * parent_index + 1
right_child_index = 2 * parent_index + 2

// Sample Tree
LIST = [5, 17, 13, 11, 1, 7, 3]
        5[0]
       /    \
    17[1]    13[2]
    /  \       /  \
 11[3] 1[4] 7[5] 3[6]
```

To heapify the binary tree, the value of the parent index must be higher than the two children. Therefore, the process starts at the bottom of the tree and works its way to the top. If the parent is smaller than one of the children values, it swaps the highest child value with the parent value. As the heapifying moves through the tree, the higher values will progressively move to the top.

When the heapifying process reaches the top, the tree is in _max heap_, where every parent-child group has the largest number as the parent. Then the top value is removed (and placed at the end of the array), and the value from the highest index (at the bottom of the tree) replaces its position at the top. Then the heapifying process begins again. 
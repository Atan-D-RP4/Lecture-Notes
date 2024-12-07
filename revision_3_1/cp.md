# SYLLABUS
## Unit-I 10 Periods
Problem Solving Paradigms:
* Overview and Motivation
* Complete Search
* Divide and Conquer
* Greedy
* Dynamic Programming
* Brute force

Sorting & Searching:
* Sorting Theory
* Counting Sort
* Radix Sort
* Heap Sort
* Bucket Sort
* Ternary Search

## Unit-II 10 Periods
Bit Manipulation:
* Bit representation
* Bit operations
* Representing Sets

Strings:
* String terminology
* Trie structures
* String hashing
* Z-algorithm

## Unit-III 10 Periods
Number theory:
* Primes and factors
* Modular arithmetic

Graphs:
* Flows and Cuts: Ford-Fulkerson algorithm Path Covers
* Paths and Circuits: Eulerian paths

## Unit-IV 10 Periods
Dynamic programming:
* Coin Problem
* Longest Increasing Sub-sequence
* Paths in a Grid
* Edit Distance
* Counting Tiles

Greedy Algorithms:
* Coin problem
* Tasks and deadlines
* Minimizing sums
* Data Compression

## Unit-V 10 Periods
Computational Geometry:
* Points and lines
* Polygon (Convex Concave)
* Distance functions

Backtracking:
* Constructing All Subsets
* Constructing All Permutations
------------------

# Notes
## Bit Manipulation
Bit Operations:
* AND
* OR
* XOR
* NOT
* Left Shift
* Right Shift

## Set Representation
Set Operations:
* Union
* Intersection
* Difference
* Complement
* Symmetric Difference

## Sorting
Radix Sort:
```python
# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.


def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix Sort


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
```
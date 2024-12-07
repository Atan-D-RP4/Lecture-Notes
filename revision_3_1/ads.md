# SYLLABUS
## Unit-I:
Skip lists and Hashing:
* Sets
* Map
* Dictionaries
* Representation of dictionary as ADT
* Linear List
* Skip List
* Hash Table Representation
* Collision Resolution Techniques.
* An application-text compression using dictionary.

## Unit-II:
Priority Queues:
* Binary heap
* Applications of binary heap
* Applications of priority queues
* Leftist heaps
* Binomial queues
Sorting:
* Shell Sort
* Indirect Sorting
* Bucket Sort
* External Sorting

## Unit-III:
Balanced Search Trees:
* Red-black trees
* Representation of Red-black tree
* Insertion, Deletion and searching of nodes in Red-black tree.
* Splay trees
* Indexed Sequential Access Method (ISAM)
* B-Trees
* B-Trees of Order m
* Representation of B-Tree
* Insertion, Deletion and searching a node in B-Tree
* B+ trees of order m
* Representation of B+-Tree
* Insertion, Deletion and searching a node in B+-Tree.

## Unit-IV:
Digital Search Structures:
* Digital Search trees,
* Binary Tries and Patricia,
* Multi-way Tries.

String Matching (Exact String Matching):
* Straight forward Algorithms
* The Knuth-Morris-Pratt Algorithm,
* The Boyer-Moore Algorithm.

## Unit-V:
Graphs:
Graph algorithms - Topological Sorting, Shortest-Path Algorithms- Unweighted Shortest
Path, Graphs with Negative Edge Cost (Bellman–Ford), Acyclic graphs, Network Flow Problems,
Applications of BFS and DFS.


### Question
Write an algorithm to perform insertion on splay trees
### Answer
Algorithm:
Perform a standard BST insert.
If the inserted node is root, return.
Else, splay the newly inserted node, that is, perform appropriate rotations to
   bring the newly inserted node to root.

Pseudocode:
```python
SplayTreeInsert(T, x)
    if T is NULL
        return x
    else
        BSTInsert(T, x)
        T = Splay(T, x)

Splay(T, x)
    if T is NULL
        return x
    if x < T
        if T.left is NULL
            T.left = x
        else
            T.left = Splay(T.left, x)
        T = RightRotate(T)
    else if x > T
        if T.right is NULL
            T.right = x
        else
            T.right = Splay(T.right, x)
        T = LeftRotate(T)
    return T

BSTInsert(T, x)
    if T is NULL
        return x
    if x < T
        T.left = BSTInsert(T.left, x)
    else if x > T
        T.right = BSTInsert(T.right, x)
    return T
```


## Question
What is a B-Tree? Specify its properties and describe the construction of a B-Tree of order 4 for the following elements.
[5, 7, 9, 10, 4, 15, 21, 3, 2, 1, 6, 8, 11, 12, 13, 14, 16, 17, 18, 19, 20]
<!--Then Delete the following elements: [17, 3]-->
## Answer
A B-Tree is a self-balancing tree data structure that maintains sorted data and
allows searches, sequential access, insertions, and deletions in logarithmic
time. The B-tree generalizes the binary search tree, allowing for nodes with
more than two children. Unlike self-balancing binary search trees, the B-tree
is well suited for storage systems that read and write relatively large blocks
of data, such as disks.

Properties of B-Tree:
1. All leaves are at the same level.
2. A non-leaf node with k children contains k-1 keys.
3. All keys of a node are sorted in increasing order.
4. All the keys in the sub-tree between the i-th child and the i-th key are less than the i-th key.
5. The root has at least two children if it is not a leaf node.
6. Each non-leaf node contains a maximum of 2t-1 keys and a minimum of t-1 keys, where t is half the order of the B-Tree.

Construction of a B-Tree of order 4 for the given elements:
```
[5, 7, 9, 10, 4, 15, 21, 3, 2, 1, 6, 8, 11, 12, 13, 14, 16, 17, 18, 19, 20]

Insert 5:
[5]

Insert 7:
[5|7]

Insert 9:
[5|7|9]

Insert 10:
[5|7|9|10]

Insert 4:
      [7]
[4|5]     [9|10]

Insert 15:
      [7]
[4|5]     [9|10|15]

Insert 21:
      [7]
[4|5]     [9|10|15|21]

Insert 3:
       [7]
[3|4|5]   [9|10|15|21]

Insert 2:
          [7]
[2|3|4|5]     [9|10|15|21]

Insert 1:
           [7]                              [3|7]
[1|2|3|4|5]   [9|10|15|21]           [1|2] [4|5] [9|10|15|21]

Insert 6:
          [3|7]
[1|2]    [4|5|6]  [9|10|15|21]

Insert 8:
          [3|7]                                [3|7|10]
[1|2]    [4|5|6]  [8|9|10|15|21]     [1|2]  [4|5|6]  [8|9]  [15|21]

Insert 11:
          [3|7|10]
[1|2]    [4|5|6]  [8|9]  [11|15|21]

Insert 12:
          [3|7|10]
[1|2]    [4|5|6]  [8|9|]  [11|12|15|21]

Insert 13:
                [3|7|10|13]
[1|2]    [4|5|6]  [8|9]  [11|12] [15|21]

Insert 14:
                [3|7|10|13]
[1|2]    [4|5|6]  [8|9]  [11|12|14] [15|21]

Insert 16:
                [3|7|10|13]
[1|2]    [4|5|6]  [8|9]  [11|12|14] [15|16|21]

Insert 17:
                [3|7|10|13]
[1|2]    [4|5|6]  [8|9]  [11|12|14] [15|16|17|21]

Insert 18:
                [3|7|10|13]
[1|2]    [4|5|6]  [8|9]  [11|12|14] [15|16|17|18|21]

                [3|7|10|13|17]
[1|2]    [4|5|6]  [8|9]  [11|12|14] [15|16] [18|21]

                    [10]
        [3|7]                   [13|17]
[1|2]    [4|5|6]  [8|9]  [11|12] [14|15|16] [18|21]

Insert 19:
                    [10]
        [3|7]                   [13|17]
[1|2]    [4|5|6]  [8|9]  [11|12] [14|15|16] [18|19|21]

Insert 20:
                    [10]
        [3|7]                   [13|17]
[1|2]    [4|5|6]  [8|9]  [11|12] [14|15|16] [18|19|20|21]

Final B-Tree after insertions:
                    [10]
        [3|7]                   [13|17]
[1|2]    [4|5|6]  [8|9]  [11|12] [14|15|16] [18|19|20|21]
```

## Question
Explain the significance of the Indexed Sequential Access Method (ISAM).

## Answer
ISAM is a method of organizing and accessing data that combines the benefits of
sequential and direct access storage methods. It uses an index to allow quick
location of records while maintaining the ability to sequentially access data.

Key Characteristics:
* Index Structure:
- The method creates a separate index file that contains key values and pointers to the actual data records
- The index serves as a lookup table, enabling rapid direct access to specific records
- Allows for quick retrieval without scanning entire files


* Data Organization:
- Records are typically stored in a sequential manner on disk
- The index provides a mapping between key values and physical record locations
- Supports both random access and sequential traversal efficiently

* Operational Mechanism:
- When searching for a record, the system first consults the index
- The index provides the exact location of the desired record
- This allows for much faster access compared to pure sequential searching

* Advantages:
- Faster data retrieval compared to pure sequential methods
- Maintains data in a logically sequential order
- Supports both random and sequential access
- Efficient for large datasets with frequent lookups

* Limitations:
- Overhead in maintaining the index
- Less efficient for very frequent insertions and deletions
- Index size can become substantial for large datasets
- Requires additional storage for the index file

* Practical Example:
Imagine a library catalog system:
- The index contains book titles (keys)
- Each index entry points to the exact shelf location
- Allows quick finding of a book without searching every shelf

## Question
Explain working principal of Knuth Morris Pratt algorithm with example.

## Answer


## Question
Define and explain the concepts of digital search trees.

## Answer
A Digital Search Tree is a Binary Tree data structure in which each node
represents a digit of a key. It is used for storing and searching keys in a
digital(binary) form, such as strings of characters or numbers. The tree is constructed
based on the digits of the keys, with each level corresponding to a different
digit position.

## Question
What are Binary Tries? Explain

## Answer
Binary Tries are a type of digital search tree where each node has at most two
children, typically representing the binary digits 0 and 1. They are used for
storing and searching binary keys, such as binary strings or numbers. The tree
is constructed based on the binary representation of the keys, with each level
corresponding to a different bit position.

## Question
How to find shortest path between two vertices using Bellman Ford algorithm?

## Answer

## Question
Write and explain breadth first algorithm with an example.

## Answer

## Question
Explain Topological sorting and state its applications.

## Answer

## Question
State Network flow problems with suitable examples.

## Answer

## Question
Explain Straight forward Algorithm with example.

## Answer

## Question
Explain Boyer-Moore Algorithm.

## Answer

## Question
Explain about Insertion operation in Patricia with an example.

## Answer

## Question
Explain M-Way Tries.

## Answer
A Multi-Way Trie (or simply a Trie) is a tree data structure used for storing
strings in a way that allows for efficient retrieval and searching. It is a
type of digital search tree where each node can have multiple children,
typically corresponding to different characters or digits. The tree is
constructed based on the characters of the keys, with each level representing a
different character position.


## Question
What is a B+-Tree? Specify its properties and describe the construction of a B+ Tree of order m for the following elements.
[5, 7, 9, 10, 4, 15, 21]

## Answer


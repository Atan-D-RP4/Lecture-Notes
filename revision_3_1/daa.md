# SYLLABUS

## UNIT- I
### Introduction:
- Introduction
- Steps for algorithmic problem solving
- Important Problem Types
- Asymptotic Notations and Efficiency Classes
- Mathematical Analysis for recursive Algorithms and Non- recursive Algorithms
- Empirical Analysis
- Algorithm Visualization

## UNIT-II:
### Brute Force:
- Selection and Bubble sort
- Sequential Search
- Closest- Pair
- Convex Hull Problem

### Exhaustive Search:
- Travelling Salesman problem
- Knapsack problem
- Assignment Problem

### Divide-and-Conquer:
- General Method
- Binary Search
- Merge sort
- Quick sort
- Stassen’s Matrix Multiplication
- Multiplication of large integers

## UNIT-III:
### Transform and conquer:
- Pre-sorting
- Gauss Elimination
- Balanced Trees – 2-3 Trees
- Heap sort
- Horner’s rule and binary exponentiation

### Problem reduction
- Least Common Multiple
- Counting paths in a graph

### Dynamic Programming:
- All Pair Shortest Path Problem
- Optimal Binary Search Trees
- 0/1 Knapsack Problem and Memory Functions

## UNIT-IV:
### Greedy Technique:
- Minimum Spanning Tree Algorithm
- Single Source Shortest Path Problem
- Huffman Trees

### Space and Time Trade-offs:
- Sorting by computing
- Input Enhancement in String Matching- Horspool’s Algorithm
- Boyer-Moore Algorithm

### Backtracking:
- N-queen problem
- Sum of subsets problem
- Graph Coloring
- Hamiltonian Cycle Problem

## UNIT-V:
### Branch and Bound:
- General method
- Applications:
    - 0/1 knapsack proble
    - Travelling salesman problem
    - Assignment Problem

### NP-HARD & NP-COMPLETE PROBLEMS:
- Lower Bound Arguments
- P, NP, NP - Hard and NP Complete classes
- Challenges in numerical algorithms


# Notes



## Unit-V
### Branch and Boumd:
1. General Method:
Branch and Bound is a general algorithm design paradigm that is used to solve
optimization problems. It works by exploring the solution space in a systematic
way, dividing it into smaller subproblems and bounding the solutions to prune
the search space efficiently.

Key Steps in Branch and Bound:
- Initialization: Initialize the algorithm with the initial problem instance.
- Branching: Divide the problem into smaller subproblems by branching on a
  variable or decision.
- Bounding: Calculate an upper or lower bound on the solution to prune the
  search space.
- Backtracking: Explore the subproblems recursively, backtracking when a
  solution is infeasible or suboptimal.
- Termination: Stop when all subproblems have been explored or the optimal
  solution is found.

Applications of Branch and Bound:
- Combinatorial Optimization: Traveling Salesman Problem, Knapsack Problem
- Scheduling Problems: Job Shop Scheduling, Task Assignment
- Integer Programming: Mixed Integer Linear Programming
- Graph Problems: Shortest Path, Minimum Spanning Tree
- Machine Learning: Decision Trees, Feature Selection

2. 0/1 Knapsack Problem:
The 0/1 Knapsack Problem is a classic optimization problem that falls under the
NP-Hard category. It involves selecting a subset of items with given weights
and values to maximize the total value while keeping the total weight within a
specified limit.

Key Concepts:
- Decision Variables: Binary variables indicating whether an item is selected
  or not
- Objective Function: Maximize the total value of selected items
- Constraints: Total weight of selected items should not exceed the knapsack
  capacity

Solving the 0/1 Knapsack Problem using Branch and Bound:
- Branching Strategy: Branch on the decision variables (item selection)
- Bounding Strategy: Calculate the upper bound based on the remaining items
- Backtracking: Explore the search space efficiently to find the optimal solution
- Termination: Stop when all subproblems have been explored


### NP-HARD, NP-COMPLETE, & Numerical Problems:
1. Lower Bound Arguments
Lower bound arguments are fundamental in computational complexity theory,
helping us understand the inherent difficulty of solving computational
problems. A lower bound is the minimum time or space complexity required to
solve a problem, regardless of the algorithm used.

Key aspects of lower bound arguments include:
- Proving Minimum Computational Complexity: Lower bounds demonstrate the
    theoretical minimum resources (time or space) needed to solve a problem.
- Proof Techniques:
  - Comparison Model: Analyzing algorithms that can only compare elements
  - Decision Tree Arguments: Examining the minimum number of decisions required to solve a problem
  - Information-Theoretic Arguments: Using information theory to establish computational limits

Classic Examples:
- Sorting Lower Bound: Comparison-based sorting algorithms have a Ω(n log n) lower bound
- Searching in Unsorted Arrays: Require Ω(n) time complexity
- Minimum number of comparisons to find the maximum in an array: Ω(n-1)

2. P, NP, NP-Hard, and NP-Complete Classes
These complexity classes are crucial in understanding computational complexity
and problem difficulty:
P (Polynomial Time):
- Problems solvable in polynomial time by a deterministic Turing machine
- Efficient, typically with complexity O(n^k) where k is a constant
- Examples: Sorting, shortest path, linear programming

NP (Nondeterministic Polynomial Time):
- Problems verifiable in polynomial time
- Can be solved by a nondeterministic Turing machine in polynomial time
- Verification is easy, but finding the solution might be hard
- Examples: Traveling Salesman Problem, Graph Coloring

NP-Hard:
- At least as hard as the hardest problems in NP
- No known polynomial-time algorithm
- Not necessarily in NP
- Example: Halting Problem

NP-Complete:
- Subset of NP-Hard problems that are also in NP
- If a polynomial-time solution is found for any NP-Complete problem, all NP
  problems can be solved in polynomial time
- Famous NP-Complete Problems:
  - Boolean Satisfiability Problem (SAT)
  - Traveling Salesman Problem
  - Graph Coloring
  - Subset Sum Problem

The P vs NP Problem:
- One of the most important open problems in computer science
- Asks whether every problem whose solution can be quickly verified can also be solved quickly
- Unsolved as of now, with a $1 million Millennium Prize for its solution

3. Challenges in Numerical Algorithms
Numerical algorithms face unique challenges due to computational limitations
and numerical precision:
Numerical Stability:
- Small changes in input can lead to large changes in output
- Rounding errors can accumulate and cause significant inaccuracies
- Examples: Matrix inversion, solving linear systems

Floating-Point Arithmetic Limitations:
- Finite precision representation
- Cannot exactly represent all real numbers
- Leads to approximation errors
- Challenges in comparing floating-point numbers

Algorithmic Challenges:
- Ill-Conditioned Problems: Small input changes cause large output variations
- Convergence Issues in Iterative Methods
- Numerical Integration Accuracy
- Eigenvalue and Eigenvector Computation
- Linear Algebra Transformations

Mitigation Strategies:
- Use of extended precision
- Error analysis techniques
- Regularization methods
- Preconditioning in linear algebra
- Adaptive algorithms

Specific Numerical Algorithm Challenges:
- Linear System Solving (Gaussian Elimination)
- Eigenvalue Computation
- Numerical Integration
- Ordinary Differential Equation Solving
- Machine Learning Optimization Algorithms

Computational Complexity Considerations:
- Time Complexity
- Space Complexity
- Numerical Stability
- Convergence Rate
- Approximation Error

These challenges require sophisticated techniques like:
- Iterative Refinement
- Preconditioning
- Regularization
- Advanced Numerical Linear Algebra Methods

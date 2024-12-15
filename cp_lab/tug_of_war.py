"""
Tug of war is a contest of brute strength, where two teams of people pull in opposite
directions on a rope. The team that succeeds in pulling the rope in their direction is
declared the winner. A tug of war is being arranged for the office picnic. The
picnickers must be fairly divided into two teams. Every person must be on one team
or the other, thenumber of people on the two teams must not differ by more than one,
and the total weightof the people on each team should be as nearly equal as possible.

Input
The input begins with a single positive integer on a line by itself indicating the number
oftest cases following, each described below and followed by a blank line.
The first line of each case contains n, the number of people at the picnic. Each of the
next n lines gives the weight of a person at the picnic, where each weight is an integer
between 1 and 450. There are at most 100 people at the picnic. Finally, there is a blank
line between each two consecutive inputs.

Output For each test case, your output will consist of a single line containing two
numbers: the total weight of the people on one team, and the total weight of the people
onthe other team. If these numbers differ, give the smaller number first. The output of
each two consecutive cases will be separated by a blank line.
Sample Input 1
1
3
100
90
200
Sample Output 1
190 200
"""

def tug_of_war(n: int, weights: list[int]) -> tuple[int, int]:
    total_weight = sum(weights)
    half_weight = total_weight // 2
    dp = [[False] * (half_weight + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(half_weight + 1):
            if j >= weights[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - weights[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    for i in range(n + 1):
        for j in range(half_weight + 1):
            if dp[i][j]:
                print('1', end=' ')
            else:
                print('0', end=' ')
        print()

    for j in range(half_weight, -1, -1):
        if dp[n][j]:
            return j, total_weight - j

    return 0, 0

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    weights = [int(input()) for _ in range(n)]
    team1, team2 = tug_of_war(n, weights)
    print(team1, team2)
    print()

# Describe the solution
"""
The problem is a variation of the 0/1 knapsack problem. The problem is to divide the
people into two teams such that the difference between the total weight of the two teams
is minimized. The total weight of the people is 450 at most. The total weight of the
people on each team should be as nearly equal as possible. The problem can be solved
using dynamic programming. The idea is to create a 2D array dp of size n + 1 x
(half_weight + 1), where n is the number of people and half_weight is the total weight
of the people divided by 2. The dp[i][j] will be True if there is a subset of people
from 1 to i whose total weight is j. The dp[i][j] can be calculated using the following
recurrence relation:
dp[i][j] = if j >= weights ? dp[i - 1][j] or dp[i - 1][j - weights[i - 1]] : dp[i - 1][j]
"""

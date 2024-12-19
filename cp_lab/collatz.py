def cycle_length(n):
    count = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count

def max_cycle_length(i, j):
    return max(cycle_length(n) for n in range(i, j + 1))

# Input for a single pair
i, j = map(int, input("Enter the pair (i j): ").split())
print(i, j, max_cycle_length(i, j))
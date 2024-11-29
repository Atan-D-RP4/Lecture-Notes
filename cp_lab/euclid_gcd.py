def gcdExtended(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y

def findMinimalSolution(a, b):
    # Get initial solution
    gcd, x, y = gcdExtended(abs(a), abs(b))
    
    # Handle negative inputs
    if a < 0: x = -x
    if b < 0: y = -y
    
    # Make sure x ≤ y
    # We can add or subtract b/gcd to x and a/gcd to y to get new solutions
    k = (y - x) // 2
    x += (b//gcd) * k
    y -= (a//gcd) * k
    
    # If still x > y, swap and negate both
    if x > y:
        x, y = -y, -x
    
    return x, y, gcd
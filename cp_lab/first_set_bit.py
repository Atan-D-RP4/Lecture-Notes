def first_set_bit(n: int) -> int:
    count = 0

    while n > 0:
        count += 1
        if n % 2 == 1:
            return count
        n /= 2
    return -1

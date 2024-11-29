# Division by binary search
def bin_div(divident: int, divisor: int) -> (int, int):

"""
int divide(int64_t dividend, int64_t divisor) {
    // Handle special cases
    if (divisor == 0) {
        printf("Error: Division by zero\n");
        return 0;
    }

    if (dividend == 0) {
        return 0;
    }

    if (dividend == INT_MIN && divisor == -1) {
        printf("Error: Integer overflow\n");
        return INT_MAX;
    }

    // Determine the sign of the result
    int64_t sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;

    // Make both dividend and divisor positive
    uint64_t u_dividend = (dividend < 0) ? -dividend : dividend;
    uint64_t u_divisor = (divisor < 0) ? -divisor : divisor;

    // Initialize the quotient
    int64_t quotient = 0;

    // Bitwise division
    while (u_dividend >= u_divisor) {
        uint64_t shift = 0;

        // Keep left-shifting the divisor until it's greater than the dividend
        while (u_dividend >= (u_divisor << shift)) {
            if (shift == 31)
                break;
            shift++;
        }

        // Update the dividend and quotient
        u_dividend -= u_divisor << (shift - 1);
        quotient += 1 << (shift - 1);
    }

    return sign * quotient;
}
"""
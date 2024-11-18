def coin_problem(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0
    
    dp = [(amount + 1)] * (amount + 1)
    dp[0] = 0

    for coin in range(len(coins)):
        for j in range(coin, amount):
            if coin > j:
                continue
            dp[j] = min(dp[j], dp[j - coin] + 1)

    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

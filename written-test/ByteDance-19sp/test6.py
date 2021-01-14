
def coinChange(money, coins):
    dp = [float("inf")] * (money + 1)
    dp[0] = 0
    for i in range(1, len(dp)):
        for coin in coins:
            if i < coin: break
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[-1]


if __name__ == "__main__":
    N = int(input())
    money = 1024 - N
    if money == 0:
        print(0)
    else:
        print(coinChange(money, [1, 4, 16, 64]))
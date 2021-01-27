coins = [1, 5, 10, 20, 50, 100]
N = int(input())
dp = [[0] * len(coins) for _ in range(N + 1)]
for j in range(len(coins)):
    dp[0][j] = 1
for i in range(len(dp)):
    dp[i][0] = 1

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = dp[i][j-1]
        if i >= coins[j]:
            dp[i][j] += dp[i - coins[j]][j]
print(dp[N][-1])
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, len(dp)):
    for j in range(1, 7):
        if i < j: break
        dp[i] += dp[i - j]
print(dp[n])
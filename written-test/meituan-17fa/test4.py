s1 = input()
s2 = input()
dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
length = 0
for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        length = max(length, dp[i][j])
print(length)
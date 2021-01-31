class Solution:
    def checkPartitioning(self, s: str) -> bool:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i, len(dp)):
                if i == j or i == j - 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        for i in range(1, len(s)):
            for j in range(i + 1, len(s)):
                if dp[0][i-1] and dp[i][j-1] and dp[j][len(s)-1]:
                    return True
        return False
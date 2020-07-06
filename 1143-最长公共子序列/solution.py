class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, clo = len(text1)+1, len(text2)+1
        dp = [[0]*clo for _ in range(row)]
        for i in range(1, row):
            for j in range(1, clo):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
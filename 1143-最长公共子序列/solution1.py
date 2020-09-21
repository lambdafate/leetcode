class Solution:
    def __init__(self):
        self.cache = {}

    # 递归+记忆
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if (text1, text2) in self.cache:
            return self.cache[(text1, text2)]
        if text1[-1] == text2[-1]:
            return 1 + self.longestCommonSubsequence(text1[:-1], text2[:-1])
        ret = max(self.longestCommonSubsequence(text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]))
        self.cache[(text1,  text2)] = ret
        return ret





    # 动态规划
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        dp = [[0]*len(text2) for _ in range(len(text1))]
        # init first line
        tmp = len(text2)
        for j in range(len(text2)):
            if text1[0] == text2[j]:
                tmp = j
                break
        for j in range(tmp, len(text2)):
            dp[0][j] = 1
        # init first clo
        tmp = len(text1)
        for i in range(len(text1)):
            if text2[0] == text1[i]:
                tmp = i
                break
        for i in range(tmp, len(text1)):
            dp[i][0] = 1
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

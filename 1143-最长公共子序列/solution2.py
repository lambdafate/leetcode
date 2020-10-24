class Solution:
    """
        dp
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        ret = 0
        dp = [[0] * len(text2) for _ in text1]
        tmp = 0
        for j in range(len(dp[0])):
            if text2[j] == text1[0]:
                tmp = 1
            dp[0][j] = tmp
        tmp = 0
        for i in range(len(dp)):
            if text1[i] == text2[0]:
                tmp = 1
            dp[i][0] = tmp
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    """
        利用函数语义递归
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        ret = self.recursion(text1, text2, 0, 0, dict())
        return ret

    def recursion(self, text1, text2, i, j, cache):
        if i >= len(text1) or j >= len(text2):
            return 0
        if (i, j) in cache:
            return cache[(i, j)]
        ret = 0
        if text1[i] == text2[j]:
            ret = 1 + self.recursion(text1, text2, i+1, j+1, cache)
        else:
            ret = max(self.recursion(text1, text2, i+1, j, cache), self.recursion(text1, text2, i, j+1, cache))
        cache[(i, j)] = ret
        return ret
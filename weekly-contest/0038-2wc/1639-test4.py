"""
    先用记忆化dfs, 再将其改为dp
    写出状态转移方程
    dp[i][j] = dp[i][j-1] + dp[i-1][j-1] * count
"""


class Solution:
    def __init__(self):
        self.cache = {}

    """
        dp + 部分查询缓存 -> 5256 ms(换成java可能会好一点), 在所有 Python3 提交中击败了10.46%的用户
        该题用时大概一小时
    """

    def numWays(self, words: List[str], target: str) -> int:
        if not target or not words:
            return 0
        dp = [[0] * len(words[0]) for _ in range(len(target))]
        for j in range(len(dp[0])):
            dp[0][j] += self.COUNT(words, j, target[0])
            # for word in words:
            #     if word[j] == target[0]:
            #         dp[0][j] += 1
            if j > 0:
                dp[0][j] += dp[0][j-1]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                count = self.COUNT(words, j, target[i])
                # 将下列查询操作转换为带缓存的查询, 这个小优化在这个二层循环中效果巨大
                # 如果使用下列操作 -> TLE
                # for word in words:
                #     if word[j] == target[i]:
                #         count += 1
                # 下面这个其实可以去掉if判断, 但是这样易于理解
                if count == 0:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1] * count
        return dp[-1][-1] % (10**9 + 7)

    def COUNT(self, words, i, target):
        count = 0
        if (target, i) in self.cache:
            return self.cache[(target, i)]
        for word in words:
            if word[i] == target:
                count += 1
        self.cache[(target, i)] = count
        return count

    """
        dfs: 超时 -> pass 70 / 89
    """

    """
    def __init__(self):
        self.cache = {}

    def numWays(self, words: List[str], target: str) -> int:
        if not target or not words:
            return 0
        ret = self.dfs(words, 0, target, 0)
        return ret % (10**9 + 7)

    def dfs(self, words, i, target, j):
        if j >= len(target):
            return 1
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        ret = 0
        for word in words:
            for index in range(i, len(word)):
                if target[j] == word[index]:
                    ret += self.dfs(words, index + 1, target, j + 1)
        self.cache[(i, j)] = ret
        return ret

    """

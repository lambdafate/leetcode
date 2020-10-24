class Solution:
    def __init__(self):
        self.cache = {}

    def minDistance(self, word1: str, word2: str) -> int:
        ret = self.recursion(word1, word2, 0, 0)
        return ret
    

    """
        把 word1[index1:] 转换为 word2[index2:] 所需要的最小操作数
    """
    def recursion(self, word1, word2, index1, index2):
        if index1 >= len(word1) or index2 >= len(word2):
            return max(len(word1)-index1, len(word2)-index2)
        if (index1, index2) in self.cache:
            return self.cache[(index1, index2)]
        i, j = index1, index2
        while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            i, j = i+1, j+1
        if i >= len(word1) or j >= len(word2):
            return self.recursion(word1, word2, i, j)
        # insert
        insert = self.recursion(word1, word2, i, j+1)
        # update
        update = self.recursion(word1, word2, i+1, j+1)
        # delete
        delete = self.recursion(word1, word2, i+1, j)
        ret = 1 + min(insert, update, delete)
        self.cache[(index1, index2)] = ret
        return ret


    """
        dp
    """
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        dp = [[0] * len(word2) for _ in word1]
        flag = False
        for j, c in enumerate(word2):
            if c == word1[0]:
                flag = True
            if flag:
                dp[0][j] = j
            else:
                dp[0][j] = j + 1
        flag = False
        for i, c in enumerate(word1):
            if c == word2[0]:
                flag = True
            if flag:
                dp[i][0] = i
            else:
                dp[i][0] = i + 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]            



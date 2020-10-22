class Solution:
    def __init__(self):
        self.cache = {}
    """
        dfs
    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        ret = self.dfs((0,0), (m-1, n-1), m, n)
        return ret

    def dfs(self, begin, end, m, n):
        if begin[0] >= m or begin[1] >= n:
            return 0
        if begin == end:
            return 1
        if begin in self.cache:
            return self.cache[begin]
        ret = self.dfs((begin[0], begin[1]+1), end, m, n) + self.dfs((begin[0]+1, begin[1]), end, m, n)
        self.cache[begin] = ret
        return ret
    
    """
        dp
    """
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

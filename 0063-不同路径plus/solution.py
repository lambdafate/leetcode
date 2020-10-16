class Solution:
    def __init__(self):
        self.cache = {}

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        ret = self.dfs(obstacleGrid, (0, 0), (len(obstacleGrid)-1, len(obstacleGrid[0])-1))
        return ret

    def dfs(self, obstacleGrid, curr, end):
        if obstacleGrid[curr[0]][curr[1]] == 1:
            return 0
        if curr == end:
            return 1
        if curr in self.cache:
            return self.cache[curr]
        ret = 0
        if curr[1] < len(obstacleGrid[0])-1:
            ret += self.dfs(obstacleGrid, (curr[0], curr[1]+1), end)
        if curr[0] < len(obstacleGrid)-1:
            ret += self.dfs(obstacleGrid, (curr[0]+1, curr[1]), end)
        self.cache[curr] = ret
        return ret
    
    
    
    
    """
        dp
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for j in range(len(dp[0])):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(len(dp)):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

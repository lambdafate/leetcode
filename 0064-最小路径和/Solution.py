class Solution:
    def __init__(self):
        self.cache = {}

    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ret = self.dfs(grid, 0, 0)
        return ret

    def dfs(self, grid, i, j):
        if i >= len(grid) or j >= len(grid[0]):
            return float("inf")
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        ret = grid[i][j]
        right = self.dfs(grid, i, j+1)
        down = self.dfs(grid, i+1, j)
        choice = min(right, down)
        if choice != float("inf"):
            ret += choice
        self.cache[(i, j)] = ret
        return ret

    # 迭代
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
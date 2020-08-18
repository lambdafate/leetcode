class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        row, clo = len(grid), len(grid[0])
        dp = [[0]*clo for _ in range(row)]
        dp[0][0] = grid[0][0]
        # first line
        for i in range(1, clo):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        # first clo
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # fix other
        for i in range(1, row):
            for j in range(1, clo):
                dp[i][j] = grid[i][j] + max(dp[i][j-1], dp[i-1][j])
        return dp[row-1][clo-1]
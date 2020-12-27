class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for j in range(len(grid[0])):
            ans.append(self.solve(grid, 0, j))
        return ans

    def solve(self, grid, i, j):
        index = grid[i][j] + j
        if index < 0 or index >= len(grid[0]):
            return -1
        if grid[i][j] + grid[i][index] == 0:
            return -1
        if i == len(grid) - 1:
            return index
        return self.solve(grid, i + 1, index)
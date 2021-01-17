class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        grid = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0:
                    grid[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    grid[i][j] = 1 + grid[i-1][j]
        size = 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(len(grid[0])):
                if grid[i][j] == 0: break
                size = max(size, grid[i][j] * (j + 1))
        return size
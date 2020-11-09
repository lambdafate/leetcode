class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n < 0:
            return []
        grid = [[0] * n for _ in range(n)]
        self.makeGrid(grid, 0, 0, 1, n)
        return grid
    
    def makeGrid(self, grid, i, j, num, length):
        if length <= 0:
            return None
        if length == 1:
            grid[i][j] = num
            return None
        # first row
        for index in range(j, j + length - 1):
            grid[i][index] = num
            num += 1
        # last clo
        for index in range(i, i + length - 1):
            grid[index][j + length - 1] = num
            num += 1
        # last row
        for index in range(j + length - 1, j, -1):
            grid[i + length - 1][index] = num
            num += 1
        # first clo
        for index in range(i + length - 1, i, -1):
            grid[index][j] = num
            num += 1
        self.makeGrid(grid, i + 1, j + 1, num, length - 2)
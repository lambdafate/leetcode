class Solution:
    def __init__(self):
        self.ret = 0
        self.directs = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, set())
                    return self.ret
        return self.ret

    def dfs(self, grid, r, c, visited):
        visited.add((r, c))
        for direct in self.directs:
            i = r + direct[0]
            j = c + direct[1]
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                self.ret += 1
                continue
            if (i, j) not in visited:
                self.dfs(grid, i, j, visited)
            
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        if not grid or not grid[0]:
            return ret
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ret += 1
                    self.mark(grid, i, j, visited)
        return ret

    def mark(self, grid, i, j, visited):
        visited.add((i, j))
        if i > 0 and grid[i-1][j] == '1' and (i-1, j) not in visited:
            self.mark(grid, i-1, j, visited)
        if i < len(grid)-1 and grid[i+1][j] == '1' and (i+1, j) not in visited:
            self.mark(grid, i+1, j, visited)
        if j > 0 and grid[i][j-1] == '1' and (i, j-1) not in visited:
            self.mark(grid, i, j-1, visited)
        if j < len(grid[0])-1 and grid[i][j+1] == '1' and (i, j+1) not in visited:
            self.mark(grid, i, j+1, visited)


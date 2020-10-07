class Solution:
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        ret = 0
        access = set()
        # init
        for j in range(len(grid[0])):
            if grid[0][j] == 0 and (0, j) not in access:
                self.mark(grid, 0, j, access)
            if grid[len(grid)-1][j] == 0 and (len(grid)-1, j) not in access:
                self.mark(grid, len(grid)-1, j, access)
        for i in range(len(grid)):
            if grid[i][0] == 0 and (i, 0) not in access:
                self.mark(grid, i, 0, access)
            if grid[i][len(grid[0])-1] == 0 and (i, len(grid[0])-1) not in access:
                self.mark(grid, i, len(grid[0])-1, access)
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1 or (i, j) in access:
                    continue
                ret += 1
                self.mark(grid, i, j, access)
        return ret

    def mark(self, grid, i, j, access):
        access.add((i, j))
        if i > 0 and grid[i-1][j] == 0 and (i-1, j) not in access:
            self.mark(grid, i-1, j, access)
        if i < len(grid)-1 and grid[i+1][j] == 0 and (i+1, j) not in access:
            self.mark(grid, i+1, j, access)
        if j > 0 and grid[i][j-1] == 0 and (i, j-1) not in access:
            self.mark(grid, i, j-1, access)
        if j < len(grid[0])-1 and grid[i][j+1] == 0 and (i, j+1) not in access:
            self.mark(grid, i, j+1, access)
        return None




    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ret = 0
        access = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 or (i, j) in access:
                    continue
                if self.dfs(grid, i, j, access):
                    ret += 1
        return ret
    
    def dfs(self, grid, i, j, access):
        access.add((i, j))
        ret = True
        if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[0])-1:
            ret = False
        if i > 0 and grid[i-1][j] == 0 and (i-1, j) not in access:
            ret = self.dfs(grid, i-1, j, access) and ret
        if i < len(grid)-1 and grid[i+1][j] == 0 and (i+1, j) not in access:
            ret = self.dfs(grid, i+1, j, access) and ret
        if j > 0 and grid[i][j-1] == 0 and (i, j-1) not in access:
            ret = self.dfs(grid, i, j-1, access) and ret
        if j < len(grid[0])-1 and grid[i][j+1] == 0 and (i, j+1) not in access:
            ret = self.dfs(grid, i, j+1, access) and ret
        return ret
    """

if __name__ == "__main__":
    test = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Solution().closedIsland(test)




# [
#     [0, 0, 1, 1, 0, 1, 0, 0, 1, 0], 
#     [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], 
#     [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
#     [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
#     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0, 1, 1, 1], 
#     [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], 
#     [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
#     [1, 1, 1, 0, 0, 1, 0, 1, 0, 1], 
#     [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
# ]

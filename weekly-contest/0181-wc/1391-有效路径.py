class Solution:
    def __init__(self):
        self.left = [0, -1]
        self.right = [0, 1]
        self.up = [-1, 0]
        self.down = [1, 0]
        self.pointers = {
            1: [self.left, self.right]
            ,2: [self.up, self.down]
            ,3: [self.left, self.down]
            ,4: [self.down, self.right]
            ,5: [self.left, self.up]
            ,6: [self.up, self.right]
        }
        self.toleft = {1, 4, 6}
        self.toright = {1, 3, 5}
        self.toup = {2, 3, 4}
        self.todown = {2, 5, 6}
        self.helper = {
            1: [self.toleft, self.toright]
            , 2: [self.toup, self.todown]
            , 3: [self.toleft, self.todown]
            , 4: [self.todown, self.toright]
            , 5: [self.toleft, self.toup]
            , 6: [self.toup, self.toright]
        }
        self.cache = {}

    def hasValidPath(self, grid):
        if not grid or not grid[0]:
            return False
        ret = self.dfs(grid, (0, 0), (len(grid)-1, len(grid[0])-1), set())
        return ret

    def dfs(self, grid, begin, end, accessed):
        if begin == end:
            return True
        if begin in self.cache:
            return self.cache[begin]
        ret = False
        accessed.add(begin)
        for i, pointer in enumerate(self.pointers[grid[begin[0]][begin[1]]]):
            newpos = (begin[0]+pointer[0], begin[1]+pointer[1])
            if newpos[0] < 0 or newpos[0] >= len(grid) or newpos[1] < 0 or newpos[1] >= len(grid[0]):
                continue
            if newpos in accessed:
                continue
            if grid[newpos[0]][newpos[1]] not in self.helper[grid[begin[0]][begin[1]]][i]:
                continue
            ret = self.dfs(grid, newpos, end, accessed)
            if ret:
                break
        self.cache[begin] = ret
        return ret
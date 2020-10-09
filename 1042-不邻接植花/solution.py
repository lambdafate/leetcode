class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ret = [0] * n
        flowers = set([1, 2, 3, 4])
        grid = [set() for _ in range(n)]
        for path in paths:
            grid[path[0]-1].add(path[1]-1)
            grid[path[1]-1].add(path[0]-1)
        self.dfs(grid, ret, set([i-1 for i in range(n)]), flowers)
        return ret
    
    """
        关于参数 select: 
            可以不使用select, 每次进入dfs时，先遍历ret获取index
            但随着数据量变大, ret增大, 时间也会增大
            leetcode测试:
                使用遍历 --> 直接超时
                使用select --> beat 100%
            O(4**N)*O(N) -> O(4**N)*O(1) 的小优化， 在数据量巨大时会体现出惊人的效果
    """
    def dfs(self, grid, ret, select, flowers):
        if len(select) == 0:
            return True
        index = select.pop()
        tmp = set()
        for i in grid[index]:
            if ret[i] != 0:
                tmp.add(ret[i])
        choices = flowers - tmp
        for choice in choices:
            ret[index] = choice
            if self.dfs(grid, ret, select, flowers):
                return True
            ret[index] = 0
        select.add(index)
        return False

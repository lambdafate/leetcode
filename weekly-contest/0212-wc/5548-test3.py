class Solution:
    def __init__(self):
        self.directs = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1)
        ]
        self.cache = set()

    def dfs(self, heights, i, j, limit, access):
        if i == len(heights)-1 and j == len(heights[0])-1:
            return True
        if (i, j) in self.cache:
            return False
        end = (len(heights)-1, len(heights[0])-1)
        indexi, indexj = i, j
        access.add((indexi, indexj))
        for direct in self.directs:
            i = indexi + direct[0]
            j = indexj + direct[1]
            if i >= 0 and i <= end[0] and j >= 0 and j <= end[1] and (i, j) not in access:
                if abs(heights[i][j]-heights[indexi][indexj]) <= limit and self.dfs(heights, i, j, limit, access):
                    return True
        access.remove((indexi, indexj))
        self.cache.add((indexi, indexj))
        return False
        
    def minimumEffortPath(self, heights):
        l, r = 0, 10**6 - 1
        while l < r:
            limit = (l + r) >> 1
            self.cache = set()
            if self.dfs(heights, 0, 0, limit, set()):
                r = limit
            else:
                l = limit + 1
        return l


    
    
    """
        # 超时
    def minimumEffortPath(self, heights):
        if not heights or not heights[0]:
            return 0
        ret = self.dfs(heights, (0, 0), (len(heights)-1, len(heights[0])-1), set())
        return ret

    def dfs(self, heights, begin, end, access):
        if begin == end:
            return 0
        access.add(begin)
        ret = float("inf")
        for index, direct in enumerate(self.directs):
            i = begin[0] + direct[0]
            j = begin[1] + direct[1]
            if i >= 0 and i <= end[0] and j >= 0 and j <= end[1] and (i, j) not in access:
                tmp = max(abs(heights[i][j] - heights[begin[0]][begin[1]]), self.dfs(heights, (i, j), end, access))   
                ret = min(ret, tmp)
        access.remove(begin)
        return ret
    """
if __name__ == "__main__":
    heights = [
        [1, 2, 1, 1, 1], 
        [1, 2, 1, 2, 1], 
        [1, 2, 1, 2, 1], 
        [1, 2, 1, 2, 1], 
        [1, 1, 1, 2, 1]
    ]
    heights2 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    ret = Solution().minimumEffortPath(heights2)
    print(ret)

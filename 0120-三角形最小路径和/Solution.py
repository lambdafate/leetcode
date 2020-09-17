class Solution:
    def __init__(self):
        self.cache = {}

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        ret = self.recursion(triangle, 0, 0)
        return ret

    def recursion(self, triangle, i, j):
        if i >= len(triangle):
            return 0
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        curr = triangle[i][j]
        left = self.recursion(triangle, i+1, j)
        right = self. recursion(triangle, i+1, j+1)
        curr += min(left, right)
        self.cache[(i, j)] = curr
        return curr

    # 迭代
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        table = [[0] * len(line) for line in triangle]
        table[0][0] = triangle[0][0]
        for i in range(1, len(table)):
            for j in range(1, len(table[i])-1):
                table[i][j] = triangle[i][j] + min(table[i-1][j-1], table[i-1][j])
            table[i][0] = triangle[i][0] + table[i-1][0]
            table[i][-1] = triangle[i][-1] + table[i-1][-1]
        return min(table[-1])
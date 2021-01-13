from typing import *

class Solution:
    def __init__(self):
        self.data = []
        self.size = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.data = [i for i in range(len(edges) + 1)]
        self.size = [1] * len(self.data)
        for edge in edges:
            p1 = self.find(edge[0])
            p2 = self.find(edge[1])
            if p1 == p2:
                return edge
            if self.size[p1] < self.size[p2]:
                self.data[p1] = p2
                self.size[p2] += self.size[p1]
            else:
                self.data[p2] = p1
                self.size[p1] += self.size[p2]
        return [-1, -1]

    def find(self, v):
        if v == self.data[v]:
            return v
        p = self.find(self.data[v])            
        self.data[v] = p
        return p

if __name__ == "__main__":
    ret = Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])
    print(ret)

class Solution:
    def __init__(self):
        self.edgeTo = []
        self.sizes = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = self.size(edges)
        self.edgeTo = [n for n in range(size + 1)]
        self.sizes = [1] * (size + 1)
        v = [0, 0]
        for edge in edges:
            p1 = self.find(edge[0])
            p2 = self.find(edge[1])
            if p1 != p2:
                # connect
                if self.sizes[p1] < self.sizes[p2]:
                    self.edgeTo[p1] = p2
                    self.sizes[p2] += self.sizes[p1]
                else:
                    self.edgeTo[p2] = p1
                    self.sizes[p1] + self.sizes[p2]
            else:
                # cycle
                v = edge
                break
        deletes = set()
        deletes.add(self.pair(v[0], v[1]))
        # print(v)
        for i in v:
            while i != self.edgeTo[i]:
                tmp, i = i, self.edgeTo[i]
                deletes.add(self.pair(tmp, i))
        # print(deletes)
        for i in range(len(edges) - 1, -1, -1):
            ret = (edges[i][0], edges[i][1])
            if ret in deletes:
                return edges[i]
        return [-1, -1]

    def find(self, i):
        while i != self.edgeTo[i]:
            i = self.edgeTo[i]
        return i

    def size(self, edges):
        size = 0
        for edge in edges:
            size = max(size, max(edge))
        return size

    def pair(self, i, j):
        return (min(i, j), max(i, j))

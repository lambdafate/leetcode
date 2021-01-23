from typing import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        op = 0
        union = UnionSet(n)
        for con in connections:
            # 查找所有的空闲(可去除)连线
            if not union.connect(con[0], con[1]):
                op += 1
        # 把所有的计算机连接起来需要的线
        # 比如最后有3组计算机, 那么就需要2根线
        need = union.group - 1
        if op >= need:
            return need
        return -1

class UnionSet:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N
        self.group = N

    def find(self, v):
        if v == self.parent[v]:
            return v
        p = self.find(self.parent[v])
        self.parent[v] = p
        return p

    def connect(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        self.group -= 1
        return True

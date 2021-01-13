from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build graph
        graph = [set() for _ in range(len(edges) + 1)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        sets = self.TpSort(graph)
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            if (edge[0], edge[1]) in sets:
                return [min(edge), max(edge)]
        return [-1, -1]

    def TpSort(self, graph):
        while True:
            v = self.find(graph)
            if v == -1: break
            n = graph[v].pop()
            graph[n].remove(v)
        ret = set()
        for i in range(len(graph)):
            for v in graph[i]:
                ret.add((i, v))
        return ret

    def find(self, graph):
        for i in range(len(graph)):
            if len(graph[i]) == 1:
                return i
        return -1


if __name__ == "__main__":
    ret = Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])
    print(ret)

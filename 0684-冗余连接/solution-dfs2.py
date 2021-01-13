from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # build graph
        graph = [set() for _ in range(len(edges) + 1)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        path = []
        if not self.dfs(graph, 1, path):
            return [-1, -1]
        i = 0
        while i < len(path) and path[i] != path[-1]:
            i += 1
        cycles = set()
        while i < len(path) - 1:
            cycles.add((path[i], path[i+1]))
            cycles.add((path[i+1], path[i]))
            i += 1
        # print(cycles)
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            if (edge[0], edge[1]) in cycles:
                return [min(edge), max(edge)]
        return [-1, -1]

    def dfs(self, graph, v, path):
        path.append(v)
        # print(path)
        for nbs in graph[v]:
            if len(path) >= 2 and path[-2] == nbs:
                continue
            if nbs in path:
                path.append(nbs)
                return True
            if self.dfs(graph, nbs, path):
                return True
        path.pop()
        return False


if __name__ == "__main__":
    ret = Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])
    print(ret)
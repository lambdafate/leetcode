class Solution:
    def __init__(self):
        self.edgeTo = []
        self.vertex = 0

    """
        利用dfs找到图中的环, 保存环中的每一条边
        要删除的边即为 在环中的边 && 该边出现在二维数组最后
    """

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = self.size(edges)
        self.edgeTo = [n for n in range(size + 1)]
        graph = [set() for _ in range(size + 1)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        if not self.dfs(graph, 1, set()):
            return [-1, -1]
        deletes = set()
        v = self.edgeTo[self.vertex]
        deletes.add(self.pair(self.vertex, v))
        while v != self.vertex:
            tmp, v = v, self.edgeTo[v]
            deletes.add(self.pair(tmp, v))
        for i in range(len(edges) - 1, -1, -1):
            ret = (edges[i][0], edges[i][1])
            if ret in deletes:
                return edges[i]
        return [-1, -1]

    def dfs(self, graph, v, visited):
        visited.add(v)
        for nbs in graph[v]:
            if self.edgeTo[v] == nbs:
                continue
            # cycle
            if nbs in visited:
                self.edgeTo[nbs] = v
                self.vertex = nbs
                return True
            else:
                self.edgeTo[nbs] = v
                if self.dfs(graph, nbs, visited):
                    return True
        return False

    def size(self, edges):
        size = 0
        for edge in edges:
            size = max(size, max(edge))
        return size

    def pair(self, i, j):
        return (min(i, j), max(i, j))

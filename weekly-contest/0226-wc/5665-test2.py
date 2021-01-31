class Solution:
    def __init__(self):
        self.ans = []

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for pair in adjacentPairs:
            if pair[0] not in graph: graph[pair[0]] = []
            if pair[1] not in graph: graph[pair[1]] = []
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
        begin = 0
        for k in graph:
            if len(graph[k]) == 1:
                begin = k
                break
        self.recursion(graph, begin, set())
        return self.ans

    def recursion(self, graph, v, visited):
        self.ans.append(v)
        visited.add(v)
        for n in graph[v]:
            if n not in visited:
                self.recursion(graph, n, visited)
                break
        return
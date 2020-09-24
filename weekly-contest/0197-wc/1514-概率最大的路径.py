class Solution:
    def __init__(self):
        self.accessed = set()
        self.cache = {}

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        ret = 0
        if start == end:
            return 1
        if start in self.cache:
            return self.cache[start]
        self.accessed.add(start)
        for i, edge in enumerate(edges):
            if start not in edge:
                continue
            another = edge[1] if start == edge[0] else edge[0]
            if another in self.accessed:
                continue
            tmp = succProb[i] * self.maxProbability(n, edges, succProb, another, end)
            ret = max(ret, tmp)
        self.accessed.remove(start)
        self.cache[start] = ret
        return ret
            
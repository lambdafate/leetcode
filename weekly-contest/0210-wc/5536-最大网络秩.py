class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]
        for road in roads:
            graph[road[0]].add(road[1])
            graph[road[1]].add(road[0])
        ret = 0
        for i in range(n):
            for j in range(i+1, n):
                tmp = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    tmp -= 1
                ret = max(ret, tmp)
        return ret
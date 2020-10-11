class Solution:
    """
        fault
    """
    def countSubgraphsForEachDiameter(self, n, edges):
        graph = [set() for _ in range(n)]
        for edge in edges:
            graph[edge[0]-1].add(edge[1]-1)
            graph[edge[1]-1].add(edge[0]-1)
        ret = [0] * (n-1)
        for i in range(len(ret)):
            length = i + 1
            visited = set()
            tmp = 0
            for node in range(n):
                if node not in visited:
                    tmp += self.dfs(graph, node, length, visited, set())
            ret[i] = tmp
        return ret

    def dfs(self, graph, node, length, visited, path_visited):
        path_visited.add(node)
        if length <= 0:
            visited.add(node)
            return 1
        ret = 0
        for n in graph[node]:
            if n not in path_visited:
                ret += self.dfs(graph, n, length-1, visited, path_visited)
        return ret

if __name__ == "__main__":
    n = 4
    edges = [[1, 2], [2, 3], [2, 4]]
    ret = Solution().countSubgraphsForEachDiameter(n, edges)
    print(ret)
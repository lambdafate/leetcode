from typing import *
RED, BLUE = -1, 1

class Solution:
    def __init__(self):
        self.graph = None
        self.ans = None
        self.stack = set()      # 当前访问路径上的边
        self.visited = {}       # 所有已经访问过的边

    def shortestAlternatingPaths(self, n, red_edges, blue_edges: List[List[int]]) -> List[int]:
        # 构造邻接矩阵
        self.graph = [[] for _ in range(n)]
        for edge in red_edges:
            self.graph[edge[0]].append((RED, edge[1]))
        for edge in blue_edges:
            self.graph[edge[0]].append((BLUE, edge[1]))
        self.ans = [-1] * n
        self.dfs(0, RED, 0)
        self.dfs(0, BLUE, 0)
        return self.ans

    def dfs(self, v, to_v_color, length):
        k = (to_v_color, v)
        # 如果(to_v_color, v)已经访问过, 并且本次length大于上次访问时的length, 则不必再次访问
        if k in self.visited and length >= self.visited[k]:
            return
        # 记录使用to_v_color访问v节点时的length
        self.visited[k] = length
        self.stack.add(k)
        if self.ans[v] == -1:
            self.ans[v] = length
        else:
            self.ans[v] = min(self.ans[v], length)
        for color, n in self.graph[v]:
            # 访问red, blue交替节点 && (color, n)不在当前访问路径上
            if color + to_v_color == 0 and (color, n) not in self.stack:
                self.dfs(n, color, length + 1)
        self.stack.remove(k)


if __name__ == "__main__":
    ret = Solution().shortestAlternatingPaths(
        3,
        [[0, 1], [1, 2]],
        [])
    print(ret)

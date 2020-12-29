from typing import *
from collections import deque
RED, BLUE = -1, 1
class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges: List[List[int]]) -> List[int]:
        # 构造邻接表, 同时记录路径颜色
        graph = [[] for _ in range(n)]
        for edge in red_edges:
            graph[edge[0]].append((RED, edge[1]))
        for edge in blue_edges:
            graph[edge[0]].append((BLUE, edge[1]))
        ans = [-1] * n
        visited = set()
        length = 0
        d = deque()
        # 初始化队列, (RED, 0), (BLUE, 0)已经访问, 不能再从其他节点到0节点
        d.append((RED, 0))
        d.append((BLUE, 0))
        visited.add((RED, 0))
        visited.add((BLUE, 0))
        while len(d) != 0:
            # 访问该层节点
            for _ in range(len(d)):
                to_v_color, v = d.popleft()
                if ans[v] == -1:
                    # 第一次访问v
                    ans[v] = length
                else:
                    # 可能有(RED, v)(visited)和(BLUE, v)(not visited)
                    # 取两种路径最小值
                    ans[v] = min(ans[v], length)
                # 加入next nodes
                for color, n in graph[v]:
                    # 只访问red, blue交替路径 && (color, n)没有访问过
                    if to_v_color + color == 0 and (color, n) not in visited:
                        visited.add((color, n))
                        d.append((color, n))
            length += 1
        return ans        

if __name__ == "__main__":
    ret = Solution().shortestAlternatingPaths(
        3,
        [[0, 1], [1, 2]],
        [])
    print(ret)

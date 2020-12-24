from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        # (num, vertex)
        heap, nums = [], []
        for i, v in enumerate(graph):
            heapq.heappush(heap, (len(v), i))
            nums.append(len(v))
        vertex = set(range(n))
        while len(vertex) > 2:
            nodes = []
            while heap and heap[0][0] == 1:    
                num, v = heapq.heappop(heap)
                vertex.remove(v)
                nodes.append(v)
            for v in nodes:
                for nbs in graph[v]:
                    if nbs in vertex:
                        nums[nbs] -= 1
                        heapq.heappush(heap, (nums[nbs], nbs))                    
        return list(vertex)


    """
    # TLE
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        graph = [set() for _ in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        h, nodes = float("inf"), []
        vertex = set(range(n))
        while vertex:
            # print(len(vertex))
            i = vertex.pop()
            height, ins = self.bfs(graph, i)
            vertex = vertex - ins
            if height < h:
                h, nodes = height, [i]
            elif height == h:
                nodes.append(i)
        return nodes

    def bfs(self, graph, node):
        visited = set()
        instead = set()
        d = deque()
        d.append(node)
        height = 0
        while len(d) != 0:
            for _ in range(len(d)):
                n = d.popleft()
                visited.add(n)
                flag = True
                for nbs in graph[n]:
                    if nbs not in visited:
                        d.append(nbs)
                        flag = False
                if flag:
                    instead.add(n)
            height += 1
        return height, instead
    """
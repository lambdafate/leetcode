"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        # copy = self.dfs(node, {})
        copy = self.bfs(node)
        return copy

    def bfs(self, node):
        visited = {}
        d = deque()
        d.append(node)
        while len(d) != 0:
            n = d.popleft()
            copy = self.deepcopy(n)
            visited[n] = copy
            for nbs in n.neighbors:
                if nbs in visited:
                    visited[nbs].neighbors.append(copy)
                    copy.neighbors.append(visited[nbs])
                elif nbs not in d:
                    d.append(nbs)
        return visited[node] 


    def dfs(self, node, visited):
        copy = self.deepcopy(node)
        visited[node] = copy
        for nbs in node.neighbors:
            if nbs in visited:
                if copy not in visited[nbs].neighbors:
                    visited[nbs].neighbors.append(copy)
                    copy.neighbors.append(visited[nbs])
            else:
                self.dfs(nbs, visited)
        return copy

    def deepcopy(self, node):
        return Node(val = node.val)
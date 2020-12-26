class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)

    def dfs(self, graph, v, visited):
        visited.add(v)
        for i in graph[v]:
            if i not in visited:
                self.dfs(graph, i, visited)

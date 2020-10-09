class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        for prerequisit in prerequisites:
            graph[prerequisit[0]].add(prerequisit[1])
        visited = set()
        for i in range(numCourses):
            if i not in visited and self.dfs(graph, i, set(), visited):
                return False
        return True

    def dfs(self, graph, v, prerequisites, visited):
        visited.add(v)
        if graph[v] & prerequisites:
            return True
        prerequisites.add(v)
        for n in graph[v]:
            if n not in visited and self.dfs(graph, n, prerequisites, visited):
                return True
        prerequisites.remove(v)
        return False

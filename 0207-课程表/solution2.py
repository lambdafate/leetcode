class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        for relation in prerequisites:
            graph[relation[1]].add(relation[0])
            inDegree[relation[0]] += 1
        zeroDegree = set()
        for i, degree in enumerate(inDegree):
            if degree == 0:
                zeroDegree.add(i)
        for _ in range(numCourses):
            if not zeroDegree:
                return False
            i = zeroDegree.pop()
            for j in graph[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    zeroDegree.add(j)
        return True


    """
    # 逆序邻接表
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init
        graph = [set() for _ in range(numCourses)]
        for relation in prerequisites:
            graph[relation[0]].add(relation[1])
        # check cycle
        for _ in range(numCourses):
            i = self.findZeroVertex(graph)
            if i is None:
                return False
            graph[i] = None
            for j, vertex in enumerate(graph):
                if vertex is not None and i in vertex:
                    graph[j].remove(i)
        return True

    def findZeroVertex(self, graph):
        for i, vertex in enumerate(graph):
            if vertex is not None and len(vertex) == 0:
                return i
        return None
    """

    
    """
    # 正序邻接表
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [set() for _ in range(numCourses)]
        # init
        for relation in prerequisites:
            graph[relation[1]].add(relation[0])
        # check cycle
        for _ in range(numCourses):
            vertex = self.findZeroVertex(graph)
            if vertex is None:
                return False
        return True

    def findZeroVertex(self, graph):
        allVertex = set()
        inDegreeVertex = set()
        for i, vertex in enumerate(graph):
            if vertex is not None:
                allVertex.add(i)
                inDegreeVertex = inDegreeVertex | vertex
        zeroVertex = allVertex - inDegreeVertex
        if not zeroVertex:
            return None
        v = zeroVertex.pop()
        graph[v] = None
        return v
    """

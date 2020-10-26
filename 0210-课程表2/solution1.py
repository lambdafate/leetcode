class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(numCourses)]
        inDegree = [0 for _ in range(numCourses)]
        zeroDegree = set()
        # init graph
        for relation in prerequisites:
            graph[relation[1]].add(relation[0])
            inDegree[relation[0]] += 1
        for i, indegree in enumerate(inDegree):
            if indegree == 0:
                zeroDegree.add(i)
        ret = []
        for _ in range(numCourses):
            if not zeroDegree:
                return []
            i = zeroDegree.pop()
            for j in graph[i]:
                inDegree[j] -= 1
                if inDegree[j] == 0:
                    zeroDegree.add(j)
            ret.append(i)
        return ret 
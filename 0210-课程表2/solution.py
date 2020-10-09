class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(numCourses)]
        for prerequisit in prerequisites:
            graph[prerequisit[0]].add(prerequisit[1])
        courses = []
        visited = set()
        for i in range(numCourses):
            if len(courses) == numCourses:
                return courses
            if i in visited:
                continue
            if self.dfs(graph, courses, i, set(), visited):
                return []
        return courses
        
    
    def dfs(self, graph, courses, targetCourse, prerequisites, visited):
        if graph[targetCourse] & prerequisites:
            return True
        prerequisites.add(targetCourse)
        for course in graph[targetCourse]:
            if course not in courses and self.dfs(graph, courses, course, prerequisites, visited):
                return True
        courses.append(targetCourse)
        visited.add(targetCourse)
        prerequisites.remove(targetCourse)
        return False

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        require = {}
        for item in prerequisites:
            if item[1] not in require:
                require[item[1]] = []
            if self.dfs(require, item[0], item[1]):
                return False
            require[item[1]].append(item[0])
        return True

    def dfs(self, require, course, prerequisit):
        pres = require.get(course, [])
        for pre in pres:
            if prerequisit == pre:
                return True
        for pre in pres:
            if self.dfs(require, pre, prerequisit):
                return True
        return False
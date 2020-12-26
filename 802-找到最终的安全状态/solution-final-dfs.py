class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ret = []
        UNSAFE, SAFE, UNKNOWN = 0, 1, 2
        status = [UNKNOWN] * len(graph)

        def dfs(v):
            if status[v] == UNSAFE or status[v] == SAFE:
                return status[v]
            status[v] = UNSAFE
            for nbs in graph[v]:
                if status[nbs] == UNSAFE:
                    return UNSAFE
                if status[nbs] == UNKNOWN and dfs(nbs) == UNSAFE:
                    return UNSAFE
            status[v] = SAFE
            return SAFE
        for i in range(len(graph)):
            if dfs(i) == SAFE:
                ret.append(i)
        return ret

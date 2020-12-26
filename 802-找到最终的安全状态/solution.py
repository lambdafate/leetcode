class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        cycle, acycle = set(), set()
        ret = []
        for i in range(len(graph)):
            if i in cycle:
                continue
            if i in acycle:
                ret.append(i)
                continue
            visited, path = set(), set()
            flag = self.cycle(graph, i, visited, path)
            if flag:
                cycle = cycle | path
                acycle = acycle | (visited - path)
            else:
                acycle = acycle | visited
                ret.append(i)
        return ret

    def cycle(self, graph, v, visited, path):
        visited.add(v)
        path.add(v)
        for nbs in graph[v]:
            if nbs in path:
                return True
            if self.cycle(graph, nbs, visited, path):
                return True
        path.remove(v)
        return False

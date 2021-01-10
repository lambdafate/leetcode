class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        union = UnionSet(len(source))
        for allow in allowedSwaps:
            union.connect(allow[0], allow[1])
        sets = union.toSets()
        count = 0
        for indexs in sets:
            source_maps = {}
            target_maps = {}
            for i in indexs:
                source_maps[source[i]] = source_maps.get(source[i], 0) + 1
                target_maps[target[i]] = target_maps.get(target[i], 0) + 1
            count += self.getSame(source_maps, target_maps)
        return len(source) - count

    def getSame(self, maps1, maps2):
        count = 0
        for k in maps1:
            if k in maps2:
                count += min(maps1[k], maps2[k])
        return count

class UnionSet(object):
    def __init__(self, N):
        self.data = list(range(N))
        self.group = N
        self.size = [1] * N

    def find(self, v):
        if v == self.data[v]:
            return v
        p = self.find(self.data[v])
        self.data[v] = p
        return p

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def connect(self, v1, v2):
        p1 = self.find(v1)
        p2 = self.find(v2)
        if p1 == p2:
            return
        if self.size[p1] < self.size[p2]:
            self.data[p1] = p2
            self.size[p2] += self.size[p1]
        else:
            self.data[p2] = p1
            self.size[p1] += self.size[p2]
        self.group -= 1

    def toSets(self):
        maps = {}
        for i in range(len(self.data)):
            root = self.find(i)
            if root in maps:
                maps[root].append(i)
            else:
                maps[root] = [i]
        return maps.values()
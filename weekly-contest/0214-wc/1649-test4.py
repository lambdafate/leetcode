class Solution:
    def __init__(self):
        self.cache = {}

    def createSortedArray(self, instructions: List[int]) -> int:
        ret = 0
        for i, n in enumerate(instructions):
            info = self.caculate(instructions, i, n)
            self.cache[n] = self.cache.get(n, 0) + 1
            ret += min(info)
        return ret % (10**9 + 7)

    def caculate(self, nums, index, n):
        ret = [0, 0]
        for k, v in self.cache.items():
            if k < n:
                ret[0] += v
            elif k > n:
                ret[1] += v
        return ret
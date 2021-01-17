class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return 0
        count = 0
        maps = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = nums[i] * nums[j]
                maps[k] = maps.get(k, 0) + 1
        for k, v in maps.items():
            if v >= 2:
                count += self.C(v, 2) * 8
        return count

    def C(self, n, m):
        if n == m: return 1
        ret = 1
        for i in range(m+1, n+1):
            ret *= i
        for i in range(n-m, 0, -1):
            ret = ret // i
        return ret
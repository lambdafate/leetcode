class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 1:
            return 1
        cache = {2, 3, 5}
        ret = 1
        for _ in range(n-1):
            ret = min(cache)
            cache.remove(ret)
            cache.add(ret * 2)
            cache.add(ret * 3)
            cache.add(ret * 5)
        return ret

class Solution:
    def minDeletions(self, s: str) -> int:
        cache = {}
        for c in s:
            if c in cache:
                cache[c] += 1
            else:
                cache[c] = 1
        times = list(cache.values())
        times.sort()
        ret = 0
        while True:
            tmp = ret
            for i in range(len(times)-1):
                if times[i] > 0 and times[i] == times[i+1]:
                    times[i] -= 1
                    ret += 1
            if tmp == ret:
                break
        return ret
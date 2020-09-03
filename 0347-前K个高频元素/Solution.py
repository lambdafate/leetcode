class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 0
            cache[num] += 1
        tmp = [(v, k) for k, v in cache.items()]
        tmp.sort(key=lambda x: x[0], reverse=True)
        ret = [tmp[i][1] for i in range(k)]
        return ret

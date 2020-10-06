class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0:1}
        ret, tmp = 0, 0
        for num in nums:
            tmp += num
            if tmp-k in cache:
                ret += cache[tmp-k]
            if tmp not in cache:
                cache[tmp] = 0
            cache[tmp] += 1
        return ret



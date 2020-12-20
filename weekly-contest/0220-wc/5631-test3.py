class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        h = [(-nums[0], 0)]
        ret = nums[0]
        for i in range(1, len(nums)):
            item = h[0]
            while item[1] < i - k:
                heapq.heappop(h)
                item = h[0]
            ret = -item[0] + nums[i]
            heapq.heappush(h, (-ret, i))
        return ret

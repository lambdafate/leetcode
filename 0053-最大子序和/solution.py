class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i]+prev)
            prev = curr
            res = max(res, curr)
        return res

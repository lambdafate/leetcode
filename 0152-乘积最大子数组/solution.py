class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0], dp2[0] = nums[0], nums[0]
        ret = dp1[0]
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp1[i] = max(nums[i], dp1[i-1]*nums[i])
                dp2[i] = min(nums[i], dp2[i-1]*nums[i])
            else:
                dp1[i] = max(nums[i], dp2[i-1]*nums[i])
                dp2[i] = min(nums[i], dp1[i-1]*nums[i])
            ret = max(ret, dp1[i])
        return ret
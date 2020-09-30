class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ret = [0]
        self.dfs(nums, 0, ret)
        return ret[0]

    """
        超时
    """
    def dfs(self, nums, prevCoins, ret):
        if len(nums) == 0:
            ret[0] = max(ret[0], prevCoins)
            return None
        for i, num in enumerate(nums):
            tmp = (nums[i-1] if i > 0 else 1) * num * (nums[i+1] if i < len(nums)-1 else 1)
            self.dfs(nums[:i]+nums[i+1:], prevCoins+tmp, ret)
        return None
class Solution:
    def __init__(self):
        self.cache = {}

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        ret = self.dfs(nums, 0, S)
        return ret

    def dfs(self, nums, index, target):
        if index >= len(nums):
            if target == 0:
                return 1
            return 0
        if (index, target) in self.cache:
            return self.cache[(index, target)]
        ret = 0
        ret += self.dfs(nums, index+1, target-nums[index])
        ret += self.dfs(nums, index+1, target+nums[index])
        self.cache[(index, target)] = ret
        return ret
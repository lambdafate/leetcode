class Solution:
    def __init__(self):
        self.cache = {0:1}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums or target <= 0:
            return 0
        nums.sort()
        ans = self.dfs(nums, target)
        return ans

    def dfs(self, nums, target):
        if target < 0:
            return 0
        if target in self.cache:
            return self.cache[target]
        ans = 0
        for num in nums:
            if num > target:
                break
            ans += self.dfs(nums, target-num)
        self.cache[target] = ans
        return ans
class Solution:
    def __init__(self):
        self.count = 0

    def waysToSplit(self, nums: List[int]) -> int:
        self.dfs(nums, 0, 0, 1)
        return self.count
    
    def dfs(self, nums, index, prevSum, last):
        if index >= len(nums):
            return
        if last == 3:
            lastSum = sum(nums[index:])
            if prevSum <= lastSum:
                self.count += 1
            return
        currSum = 0
        for i in range(index, len(nums) - 1):
            currSum += nums[i]
            if prevSum <= currSum:
                self.dfs(nums, i + 1, currSum, last + 1)
        
class Solution:
    def __init__(self):
        self.cache = {}

    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) < 2:
            return False
        tmp = sum(nums)
        if tmp % 2 == 1:
            return False
        targetSum = tmp // 2
        ret = self.trace(nums, 0, 0, targetSum)
        return ret
        

    def trace(self, nums, index, currSum, targetSum):                                                                                             
        if currSum == targetSum:
            return True
        if currSum > targetSum or index >= len(nums):
            return False
        if (index, currSum) in self.cache:
            return self.cache[(index, currSum)]
        ret0 = self.trace(nums, index+1, currSum+nums[index], targetSum)
        if not ret0:
            ret0 = self.trace(nums, index+1, currSum, targetSum)
        self.cache[(index, currSum)] = ret0
        return ret0

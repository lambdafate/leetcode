class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        Solution.ret = 0
        ret = self.helper(nums, 0, 0, S, {})
        return ret


    
    def helper(self, nums, index, baseSum, target, fuck):
        if index >= len(nums):
            if baseSum == target:
                return 1
            return 0
        t = (index, baseSum)
        if t in fuck:
            return fuck[t]
        ret = 0
        ret += self.helper(nums, index+1, baseSum + nums[index], target, fuck)
        ret += self.helper(nums, index+1, baseSum - nums[index], target, fuck)
        fuck[(index, baseSum)] = ret
        return ret
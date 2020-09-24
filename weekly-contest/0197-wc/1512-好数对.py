class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    ret += 1
        return ret
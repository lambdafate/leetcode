class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for i in range(len(l)):
            tmp = self.check(nums[l[i]:r[i]+1])
            ret.append(tmp)
        return ret

    def check(self, nums):
        if len(nums) <= 2:
            return True
        nums.sort()
        target = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] != target:
                return False
        return True
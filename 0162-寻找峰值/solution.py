class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        for i, num in enumerate(nums):
            if i == 0 and num > nums[i+1]:
                return i
            if i == len(nums)-1 and num > nums[i-1]:
                return i
            if num > nums[i-1] and num > nums[i+1]:
                return i
        return -1

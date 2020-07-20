class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        helper = {}
        for num in nums:
            if num in helper:
                return num
            helper[num] = 0
        
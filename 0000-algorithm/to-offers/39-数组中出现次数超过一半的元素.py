class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        helper = {}
        length = len(nums) // 2
        for num in nums:
            if num not in helper:
                helper[num] = 0
            helper[num] += 1
            if helper[num] > length:
                return num
        
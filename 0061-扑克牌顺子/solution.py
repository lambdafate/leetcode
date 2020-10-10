class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        sp, blocks = 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                sp += 1
                continue
            if i > 0 and num == nums[i-1]:
                return False
            if i > 0 and nums[i-1] != 0:
                block = num - nums[i-1] - 1
                blocks += block
        blocks -= sp
        return blocks <= 0
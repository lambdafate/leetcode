class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        index = 0
        while nums and len(nums) != 1:
            index = (index + m - 1) % len(nums)
            del nums[index]
        return nums[0]
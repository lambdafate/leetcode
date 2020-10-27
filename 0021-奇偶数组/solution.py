class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 == 1:
                i += 1
                continue
            while j > i and nums[j] % 2 == 0:
                j -= 1
            if j > i:
                nums[i], nums[j] = nums[j], nums[i]
        return nums
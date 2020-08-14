class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[j] % 2 == 0:
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        return nums

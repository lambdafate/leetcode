class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        left = len(nums)-1
        right, flag = left, left
        for i in range(len(nums)-1, -1, -1):
            if nums[flag] > nums[i]:
                left, right = i, flag
            elif nums[flag] < nums[i]:
                flag = i
        nums[left], nums[right] = nums[right], nums[left]
        return int("".join(nums))
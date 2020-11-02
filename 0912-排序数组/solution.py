class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.QuickSort(nums, 0, len(nums) - 1)
        return nums

    def QuickSort(self, nums, i, j):
        if i < 0 or j >= len(nums) or i >= j:
            return None
        mark = nums[i]
        begin, end = i + 1, j
        while begin < end:
            while begin < end and nums[begin] < mark:
                begin += 1
            while begin < end and nums[end] >= mark:
                end -= 1
            nums[begin], nums[end] = nums[end], nums[begin]
        index = begin
        if nums[begin] <= mark:
            nums[begin], nums[i] = nums[i], nums[begin]
        else:
            nums[begin-1], nums[i] = nums[i], nums[begin-1]
            index -= 1
        self.QuickSort(nums, i, index - 1)
        self.QuickSort(nums, index + 1, j)

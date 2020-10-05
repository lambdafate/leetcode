class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cache = set(nums)
        for i in range(1, len(nums)+1):
            if i not in cache:
                return i
        return len(nums)+1
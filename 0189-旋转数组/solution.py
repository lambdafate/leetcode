class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        k = k % len(nums)
        i = len(nums) - k
        tmp = nums[i:] + nums[:i]
        for i in range(len(nums)):
            nums[i] = tmp[i]
        return None

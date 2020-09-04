class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num, min_num = 1, 1
        ret = float("-inf")
        for num in nums:
            if num >= 0:
                max_num = max(max_num * num, num)
                min_num = min(min_num * num, num)
            else:
                max_num, min_num = max(min_num * num, num), min(max_num * num, num)
            ret = max(ret, max_num)
        return ret


    """
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ret = nums[0]
        for i in range(0, len(nums)):
            tmp = 1
            for j in range(i, len(nums)):
                tmp = tmp * nums[j]
                ret = max(ret, tmp)
        return ret
    """

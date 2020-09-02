class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mulitSum = 1
        zero = 0
        for num in nums:
            if num != 0:
                mulitSum = mulitSum * num
            else:
                zero += 1
        ret = [0] * len(nums)
        if zero == 1:
            ret[nums.index(0)] = mulitSum
        if zero > 0:
            return ret
        for i, num in enumerate(nums):
            ret[i] = mulitSum // num
        return ret
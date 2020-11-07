"""
    同样的暴力算法, python TLE, java ac
"""
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        ret = 0
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
                if tmp >= lower and tmp <= upper:
                    ret += 1
        return ret
"""
    https://stackoverflow.com/questions/24578896/python-built-in-sum-function-vs-for-loop-performance
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maps = {}
        tmpValue = 0
        ret = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] in maps and maps[nums[i]] + length >= i:
                length = i - maps[nums[i]]
                maps[nums[i]] = i
                # sum is better than loop
                tmpValue = sum(nums[i+1-length:i+1])
                # tmpValue = 0
                # for j in range(i, i - length, -1):
                #     tmpValue += nums[j]
            else:
                length += 1
                maps[nums[i]] = i
                tmpValue += nums[i]
            ret = max(ret, tmpValue)
        return ret

"""
from collections import deque

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = deque()
        ret = float("-inf")
        for num in nums:
            if num in d:
                while d.popleft() != num:
                    pass
                d.append(num)
            else:
                d.append(num)
            ret = max(ret, sum(d))
        return ret
"""

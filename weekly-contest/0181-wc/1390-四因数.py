import math


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ret = 0
        for num in nums:
            ret += self.isValid(num)
        return ret


    def isValid(self, num):
        ret = set([1, num])
        i, end = 2, int(math.sqrt(num))
        while i <= end:
            if num % i != 0:
                i += 1
                continue
            ret.add(i)
            ret.add(num // i)
            i += 1
            if len(ret) > 4:
                return 0
        return sum(ret) if len(ret) == 4 else 0


import math
import sys

class Solution:
    def __init__(self):
        self.cache = {}

    def numSquares(self, n):
        if n < 4:
            return n
        if n in self.cache:
            return self.cache[n]
        tmp = int(math.sqrt(n))
        ret = sys.maxsize
        for i in range(tmp, 0, -1):
            ret = min(1 + self.numSquares(n-i**2), ret)
        self.cache[n] = ret
        return ret



    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            if i < 4:
                dp[i] = i
                continue
            tmp = int(math.sqrt(i))
            curr = sys.maxsize
            for j in range(1, tmp+1):
                curr = min(curr, dp[i - j**2]+1)
            dp[i] = curr
        return dp[n]

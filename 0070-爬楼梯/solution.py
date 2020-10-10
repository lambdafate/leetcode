class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n <= 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if n in self.cache:
            return self.cache[n]
        ret = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = ret
        return ret

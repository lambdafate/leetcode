class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        if n in self.cache:
            return self.cache[n]
        ret = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.cache[n] = ret
        return ret
    
    # 迭代
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n+1):
            if i >= 1:
                dp[i] += dp[i-1]
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
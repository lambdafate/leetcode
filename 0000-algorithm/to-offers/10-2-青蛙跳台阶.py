class Solution:
    # 每次求解只需要前面的两个解
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        i, j = 1, 1
        for _ in range(2, n+1):
            j, i = i+j, j
            j %= 1000000007
        return j


    """
    def numWays(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] %= 1000000007
        return dp[n]
    """

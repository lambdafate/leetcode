class Solution:
    def numSub(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        prev = -1
        MASK = 10**9 + 7 
        for i in range(1, len(dp)):
            if s[i-1] == '0':
                dp[i] = dp[i-1]
                prev = i - 1
                continue
            length = i - 1 - prev
            dp[i] = dp[i-1] + length
        return dp[-1] % MASK
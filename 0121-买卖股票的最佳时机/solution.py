class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        if len(prices) < 2:
            return ret
        dp = [0] * len(prices)
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], prices[i]-min(prices[:i]))
            ret = max(ret, dp[i])
        return ret

    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        buy = float("inf")
        for i, price in enumerate(prices):
            if price <= buy:
                buy = price
            else:
                ret = max(ret, price - buy)
        return ret
                

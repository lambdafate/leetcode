class Solution:
    """
        dp
    """
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        minprices = prices[0]
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = max(dp[i-1], prices[i]-minprices)
            minprices = min(minprices, prices[i])
        return dp[-1]


    """
        低买高抛
    """
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                profit = max(profit, prices[j]-prices[i])
            else:
                i = j
        return profit

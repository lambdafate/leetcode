class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit, buy = 0, prices[0]
        for price in prices:
            profit = max(profit, price-buy)
            buy = min(buy, price)
        return profit

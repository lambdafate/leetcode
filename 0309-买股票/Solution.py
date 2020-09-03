class Solution:
    def __init__(self):
        self.cache = {}

    def maxProfit(self, prices: List[int]) -> int:
        profit = self.maxProfitFromDay(prices, 0)
        return profit

    def maxProfitFromDay(self, prices, day):
        if day >= (len(prices)-1):
            return 0
        if day in self.cache:
            return self.cache[day]
        profit = 0
        buy = prices[day]
        for i in range(day+1, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
                continue
            profit_tmp = prices[i] - buy + self.maxProfitFromDay(prices, i+2)
            profit = max(profit, profit_tmp)
        self.cache[day] = profit
        return profit


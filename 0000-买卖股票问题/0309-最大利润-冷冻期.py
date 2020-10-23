class Solution:
    def __init__(self):
        self.cache = {}

    def maxProfit(self, prices: List[int]) -> int:
        profit = self.getMaxProfit(prices, 0)
        return profit

    def getMaxProfit(self, prices, index):
        if index >= len(prices)-1:
            return 0
        if index in self.cache:
            return self.cache[index]
        profit = 0
        i = index
        for j in range(index+1, len(prices)):
            if prices[j] > prices[i]:
                profit = max(
                    profit, prices[j]-prices[i] + self.getMaxProfit(prices, j+2))
            else:
                i = j
        self.cache[index] = profit
        return profit

class Solution:
    def __init__(self):
        self.cache = {}
    """
    # 递归
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.cache:
            return self.cache[amount]
        ret = float("inf")
        for coin in coins:
            if amount >= coin:
                tmp = self.coinChange(coins, amount-coin)
                if tmp != -1:
                    ret = min(ret, tmp+1)
        ret = -1 if ret == float("inf") else ret
        self.cache[amount] = ret
        return ret
    """

    # 迭代
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        coins.sort()
        dp = [-1] * (amount+1)
        dp[0] = 0
        for totalMoney in range(coins[0], amount+1):
            tmp = float("inf")
            for coin in coins:
                if totalMoney < coin:
                    break
                if dp[totalMoney-coin] != -1:
                    tmp = min(tmp, 1+dp[totalMoney-coin])
            if tmp != float("inf"):
                dp[totalMoney] = tmp
        return dp[amount]

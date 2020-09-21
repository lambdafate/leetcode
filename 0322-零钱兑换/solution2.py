class Solution:
    def __init__(self):
        self.cache = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in self.cache:
            return self.cache[amount]
        ret = float("inf")
        for coin in coins:
            tmp = self.coinChange(coins, amount-coin)
            if tmp != -1:
                ret = min(ret, 1+tmp)
        ret = -1 if ret == float("inf") else ret
        self.cache[amount] = ret
        return ret

    """
        dp
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return -1
        dp = [-1] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for money in range(1, amount+1):
            tmp = float("inf")
            for coin in coins:
                if money < coin:
                    break
                if dp[money-coin] == -1:
                    continue
                tmp = min(tmp, 1+dp[money-coin])
            dp[money] = -1 if tmp == float("inf") else tmp
        return dp[-1]
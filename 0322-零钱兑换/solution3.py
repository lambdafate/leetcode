class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        coins.sort()
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            ret = float("inf")
            for coin in coins:
                if coin > i:
                    break
                tmp = dp[i-coin]
                if tmp != -1:
                    ret = min(ret, 1+tmp)
            if ret != float("inf"):
                dp[i] = ret
        return dp[-1]




    def __init__(self):
        self.cache = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        coins.sort()
        ret = self.dfs(coins, amount)
        return ret

    def dfs(self, coins, amount):
        if amount == 0:
            return 0
        if amount in self.cache:
            return self.cache[amount]
        ret = float("inf")
        for coin in coins:
            if coin > amount:
                break
            tmp = self.dfs(coins, amount-coin)
            if tmp != -1:
                ret = min(ret, 1 + tmp)
        ret = -1 if ret == float("inf") else ret
        self.cache[amount] = ret
        return ret

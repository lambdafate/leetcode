class Solution:
    """
        dp
    """

    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j >= coins[i-1]:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        dp = [[0]*(len(coins)+1) for _ in range(amount+1)]
        dp[0] = [1] * (len(dp[0]))
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                tmp = 0
                for index in range(j, 0, -1):
                    coin = coins[index-1]
                    if coin > i:
                        break
                    tmp += dp[i-coin][index]
                dp[i][j] = tmp
        return dp[-1][-1]

    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        ret = self.recursion(coins, amount, 0, {})
        return ret

    def recursion(coins, amount, index, cache):
        if amount == 0:
            return 1
        if index >= len(coins):
            return 0
        if (amount, index) in cache:
            return cache[(amount, index)]
        ret = 0
        for i in range(index, len(coins)):
            if coins[i] > amount:
                break
            ret += self.recursion(coins, amount-coins[i], i, cache)
        cache[(amount, index)] = ret
        return ret

class Solution:
    def waysToChange(self, n):
        dp = [1] + [0 for _ in range(n)]
        coins = [1, 5, 10, 25]
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = (dp[i] + dp[i-coin]) % 1000000007

        print(f"dp => {dp}")
        return dp[n]


if __name__ == "__main__":
    print(float("inf"))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # init
        dp[0][0] = True
        for j in range(1, len(dp[0])):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if p[j-1] == "*":
                    if self.match(p[j-2], s[i-1]):
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
                elif self.match(p[j-1], s[i-1]):
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

    def match(self, c1, c2):
        return c1 == "." or c1 == c2

if __name__ == "__main__":
    s = "a"
    p = "a*a"
    match = Solution()
    ans = match.isMatch(s, p)
    print(ans)
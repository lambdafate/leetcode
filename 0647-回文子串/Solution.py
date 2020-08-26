class Solution:
    # 动态规划
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        dp = [[False] * len(s) for _ in s]
        res = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                """
                if i == j:
                    pass
                if i == j-1 and s[i] == s[j]:
                    pass
                if s[i] == s[j] and dp[i+1][j-1]:
                    pass
                """
                if (i == j) or (s[i] == s[j] and (i == j-1 or dp[i+1][j-1])):
                    res += 1
                    dp[i][j] = True
        return res

    # 暴力
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        for i in range(len(s)):
            tmp = 1
            for j in range(i+1, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    tmp += 1
            res += tmp
        return res

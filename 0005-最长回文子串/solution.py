class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(dp)):
            dp[i][i] = True
        begin, end = 0, 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if j == i+1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and (dp[i+1][j-1])
                if dp[i][j] and j-i >= end-begin:
                    begin, end = i, j
        return s[begin:end+1]

    def longestPalindrome(self, s: str) -> str:
        ret = ""
        if not s:
            return ret
        for i in range(len(s)):
            for j in range(i, len(s)):
                tmp = s[i:j+1]
                if tmp == tmp[::-1] and len(tmp) > len(ret):
                    ret = tmp
        return ret

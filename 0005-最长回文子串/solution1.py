class Solution:
    """
        中心扩散
    """
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        begin, end = 0, 0
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and s[left] == s[i]:
                left -= 1
            while right < len(s) and s[right] == s[i]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) >= (end - begin + 1):
                end = right - 1
                begin = left + 1
        return s[begin:end+1]
    
    
    
    """
        动态规划
    """
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        dp = [[False]*len(s) for _ in s]
        ret = (0, 0)
        for i in range(len(dp)-1, -1, -1):
            for j in range(i, len(dp)):
                if i == j:
                    dp[i][j] = True
                elif i == j-1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j] and (j-i+1) >= (ret[1] - ret[0] + 1):
                    ret = (i, j)  
        return s[ret[0]:ret[1]+1]
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp  = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        ret = 0
        for i in range(len(dp)):
            dp[i][0] = int(matrix[i][0])
            ret = max(ret, dp[i][0])
        for j in range(len(dp[0])):
            dp[0][j] = int(matrix[0][j])
            ret = max(ret, dp[0][j])
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                ret = max(ret, dp[i][j])
        return ret**2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix[0]) == 0:
            return 0
        dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for i in range(len(dp)):
            dp[i][0] = 0
        for j in range(len(dp[0])):
            dp[0][j] = 0
        length = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    length = max(length, dp[i][j])
        return length**2

    # 暴力
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ret = 0
        if not matrix or len(matrix[0]) == 0:
            return ret
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    tmp = self.maxSquare(matrix, i, j)
                    ret = max(ret, tmp)
        return ret

    def maxSquare(self, matrix, i, j):
        length = 1
        tmp_i, tmp_j = i+1, j+1
        while tmp_i < len(matrix) and tmp_j < len(matrix[0]):
            if matrix[tmp_i][tmp_j] == '0':
                return length**2
            for row in range(tmp_i-1, i-1, -1):
                if matrix[row][tmp_j] == '0':
                    return length**2
            for clo in range(tmp_j-1, j-1, -1):
                if matrix[tmp_i][clo] == '0':
                    return length**2
            length += 1
            tmp_i, tmp_j = tmp_i+1, tmp_j+1
        return length**2

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if matrix is None or len(matrix) == 0:
            return res
        self.helper(0, 0, matrix, res)
        return res

    def helper(self, i, j, matrix, result):
        row, clo = len(matrix)-1, len(matrix[0])-1
        if i > (row // 2) or j > (clo // 2):
            return
        if i == (row // 2) and row % 2 == 0:
            result.extend([matrix[i][c] for c in range(j, clo-j+1)])
            return
        if j == (clo // 2) and clo % 2 == 0:
            result.extend([matrix[r][j] for r in range(i, row+1-i)])
            return
        for c in range(j, clo-j):
            result.append(matrix[i][c])
        for r in range(i, row-i):
            result.append(matrix[r][clo-j])
        for c in range(clo-j, j, -1):
            result.append(matrix[row-i][c])
        for r in range(row-i, i, -1):
            result.append(matrix[r][j])
        self.helper(i+1, j+1, matrix, result)

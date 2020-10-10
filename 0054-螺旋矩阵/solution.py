class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        if not matrix:
            return ret
        self.helper(matrix, 0, 0, len(matrix), len(matrix[0]), ret)
        return ret
    
    def helper(self, matrix, i, j, m, n, ret):
        if m <= 0 or n <= 0:
            return
        if m == 1:
            ret.extend(matrix[i][j:j+n])
            return
        elif n == 1:
            tmp = []
            for index in range(i, i+m):
                tmp.append(matrix[index][j])
            ret.extend(tmp)
            return
        tmp = []
        for clo in range(j, j+n-1):
            tmp.append(matrix[i][clo])
        for row in range(i, i+m-1):
            tmp.append(matrix[row][j+n-1])
        for clo in range(j+n-1, j, -1):
            tmp.append(matrix[i+m-1][clo])
        for row in range(i+m-1, i, -1):
            tmp.append(matrix[row][j])
        ret.extend(tmp)
        self.helper(matrix, i+1, j+1, m-2, n-2, ret)





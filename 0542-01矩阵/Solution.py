class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                self.BFS(matrix, i, j)
        return matrix

    def BFS(self, matrix, i, j):
        queue = [(i, j, 0)]
        accessd = set()
        index = 0
        while index < len(queue):
            r, c, length_to_point = queue[index]
            if (r, c) in accessd:
                index += 1
                continue
            if matrix[r][c] == 0:
                matrix[i][j] = length_to_point
                break
            accessd.add((r, c))
            if r > 0:
                queue.append((r-1, c, length_to_point+1))
            if c > 0:
                queue.append((r, c-1, length_to_point+1))
            if r < len(matrix)-1:
                queue.append((r+1, c, length_to_point+1))
            if c < len(matrix[0])-1:
                queue.append((r, c+1, length_to_point+1))
            index += 1
        return None
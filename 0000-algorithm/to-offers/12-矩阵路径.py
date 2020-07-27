class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, clo = len(board), len(board[0])
        bits = [[0]*clo for _ in range(row)]
        for i in range(row):
            for j in range(clo):
                if board[i][j] == word[0]:
                    bits[i][j] = 1
                    if self.backtrace(board, i, j, word, 1, bits):
                        return True
                    bits[i][j] = 0
        return False

    def backtrace(self, board, i, j, word, index, bits):
        if index == len(word):
            return True
        row, clo = len(board)-1, len(board[0])-1
        if i > 0 and board[i-1][j] == word[index] and bits[i-1][j] == 0:
            bits[i-1][j] = 1
            if self.backtrace(board, i-1, j, word, index+1, bits):
                return True
            bits[i-1][j] = 0
        if j > 0 and board[i][j-1] == word[index] and bits[i][j-1] == 0:
            bits[i][j-1] = 1
            if self.backtrace(board, i, j-1, word, index+1, bits):
                return True
            bits[i][j-1] = 0
        if i < row and board[i+1][j] == word[index] and bits[i+1][j] == 0:
            bits[i+1][j] = 1
            if self.backtrace(board, i+1, j, word, index+1, bits):
                return True
            bits[i+1][j] = 0
        if j < clo and board[i][j+1] == word[index] and bits[i][j+1] == 0:
            bits[i][j+1] = 1
            if self.backtrace(board, i, j+1, word, index+1, bits):
                return True
            bits[i][j+1] = 0
        return False

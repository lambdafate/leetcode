class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board[0]) == 0 or not word:
            return False
        comepath = [[False]*(len(board[0])) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.backtrace(board, i, j, word, 1, comepath):
                    return True
        return False

    def backtrace(self, board, i, j, word, index, comepath):
        if index >= len(word):
            return True
        comepath[i][j] = True
        if i > 0 and board[i-1][j] == word[index] and not comepath[i-1][j]:
            if self.backtrace(board, i-1, j, word, index+1, comepath):
                return True
        if i < len(board)-1 and board[i+1][j] == word[index] and not comepath[i+1][j]:
            if self.backtrace(board, i+1, j, word, index+1, comepath):
                return True
        if j > 0 and board[i][j-1] == word[index] and not comepath[i][j-1]:
            if self.backtrace(board, i, j-1, word, index+1, comepath):
                return True
        if j < len(board[0])-1 and board[i][j+1] == word[index] and not comepath[i][j+1]:
            if self.backtrace(board, i, j+1, word, index+1, comepath):
                return True
        comepath[i][j] = False
        return False  
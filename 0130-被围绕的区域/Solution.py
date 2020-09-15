class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return board
        def dfs(board, i, j):
            if i < 0 or i == len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = '#'
            dfs(board, i-1, j)
            dfs(board, i+1, j)
            dfs(board, i, j-1)
            dfs(board, i, j+1)
        for j in range(len(board[0])):
            dfs(board, 0, j)
            dfs(board, len(board)-1, j)
        for i in range(len(board)):
            dfs(board, i, 0)
            dfs(board, i, len(board[0])-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return None
        

    """
    def solve(self, board: List[List[str]]) -> None:
        """
        #   Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        row, clo = len(board), len(board[0])
        accessd = [[False] * clo for _ in range(row)]
        cache = set()
        for i in range(1, row-1):
            for j in range(1, clo-1):
                if board[i][j] == 'X':
                    continue
                paths = []
                if self.dfs(board, accessd, row, clo, i, j, cache, paths):
                    for r, c in paths:
                        board[r][c] = 'X'
                else:
                    cache.add((i, j))
    def dfs(self, board, accessd, row, clo, i, j, cache, paths):
        if board[i][j] == 'X':
            return True
        if (i, j) in cache:
            return False
        if i == 0 or i == (row-1) or j == 0 or j == (clo-1):
            return False
        accessd[i][j] = True
        if not accessd[i-1][j] and not self.dfs(board, accessd, row, clo, i-1, j, cache, paths):
            accessd[i][j] = False
            return False
        if not accessd[i+1][j] and not self.dfs(board, accessd, row, clo, i+1, j, cache, paths):
            accessd[i][j] = False
            return False
        if not accessd[i][j-1] and not self.dfs(board, accessd, row, clo, i, j-1, cache, paths):
            accessd[i][j] = False
            return False
        if not accessd[i][j+1] and not self.dfs(board, accessd, row, clo, i, j+1, cache, paths):
            accessd[i][j] = False
            return False
        accessd[i][j] = False
        paths.append((i, j))
        return True

    """
if __name__ == "__main__":
    board = [
        ["X", "X", "X", "X", "O", "O", "X", "X", "O"], 
        ["O", "O", "O", "O", "X", "X", "O", "O", "X"], 
        ["X", "O", "X", "O", "O", "X", "X", "O", "X"], 
        ["O", "O", "X", "X", "X", "O", "O", "O", "O"], 
        ["X", "O", "O", "X", "X", "X", "X", "X", "O"], 
        ["O", "O", "X", "O", "X", "O", "X", "O", "X"], 
        ["O", "O", "O", "X", "X", "O", "X", "O", "X"], 
        ["O", "O", "O", "X", "O", "O", "O", "X", "O"], 
        ["O", "X", "O", "O", "O", "X", "O", "X", "O"]
        ]
                                                                                                                                                                                                          "X", "X", "X", "X", "O"], ["O", "O", "X", "O", "X", "O", "X", "O", "X"], ["O", "O", "O", "X", "X", "O", "X", "O", "X"], ["O", "O", "O", "X", "O", "O", "O", "X", "O"], ["O", "X", "O", "O", "O", "X", "O", "X", "O"]]

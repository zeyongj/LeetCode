class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        if rows == 0 or cols == 0:
            return
        
        for i in range(rows):
            self.dfs(board, i, 0)
            self.dfs(board, i, cols - 1)
        for j in range(cols):
            self.dfs(board, 0, j)
            self.dfs(board, rows - 1, j)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                    
    def dfs(self, board, i, j):
        rows = len(board)
        cols = len(board[0])
        
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
            return
        
        board[i][j] = '#'
        
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)        
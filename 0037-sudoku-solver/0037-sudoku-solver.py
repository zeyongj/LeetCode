class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            for x in range(9):
                if board[row][x] == num:
                    return False
                    
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            start_row, start_col = row - row%3, col - col%3
            for i in range(3):
                for j in range(3):
                    if board[i+start_row][j+start_col] == num:
                        return False
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in "123456789":
                            if is_valid(board, i, j, num):
                                board[i][j] = num

                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'  # undo if no valid number can be placed
                        return False  # trigger backtracking
            return True  # all cells are filled
            
        solve(board)

        
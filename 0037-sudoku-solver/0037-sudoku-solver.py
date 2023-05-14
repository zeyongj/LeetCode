class Solution:
    def solveSudoku(self, board):
        def is_valid(board, row, col, num):
            # Check the number in the row
            for x in range(9):
                if board[row][x] == num:
                    return False
                    
            # Check the number in the col
            for x in range(9):
                if board[x][col] == num:
                    return False
            
            # Check the number in the box
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
                                board[i][j] = num  # attempt this number for the cell

                                if solve(board):  # continue with this number for the cell
                                    return True
                                
                                else:
                                    board[i][j] = '.'  # undo if this number didn't lead to a solution
                        return False  # trigger backtracking from previous cell
            return True  # entire board has been filled
        
        if not board:
            return
        solve(board)

class Solution:
    def solveNQueens(self, n: int):
        def could_place(row, col):
            for i in range(row):
                if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                    return False
            return True
        
        def place_queen(row, n):
            for col in range(n):
                if could_place(row, col):
                    board[row] = col
                    if row + 1 == n:
                        result.append(board[:])
                    else:
                        place_queen(row + 1, n)
        
        def to_result(board):
            res = []
            for i in board:
                res.append("." * i + "Q" + "." * (n - 1 - i))
            return res

        result = []
        board = [-1] * n
        place_queen(0, n)
        return [to_result(sol) for sol in result]

func solveSudoku(board [][]byte) {
    solve(board)
}

func solve(board [][]byte) bool {
    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            if board[i][j] == '.' {
                for c := byte('1'); c <= '9'; c++ {
                    if isValid(board, i, j, c) {
                        board[i][j] = c

                        if solve(board) {
                            return true
                        }

                        board[i][j] = '.'
                    }
                }
                return false
            }
        }
    }
    return true
}

func isValid(board [][]byte, row, col int, c byte) bool {
    for i := 0; i < 9; i++ {
        if board[i][col] == c {
            return false
        }
        if board[row][i] == c {
            return false
        }
        if board[3*(row/3)+i/3][3*(col/3)+i%3] == c {
            return false
        }
    }
    return true
}

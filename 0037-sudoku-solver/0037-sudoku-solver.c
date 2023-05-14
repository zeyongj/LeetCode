bool is_valid(char** board, int row, int col, char c) {
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == c) return false; // check column
        if (board[row][i] == c) return false; // check row
        if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) return false; // check 3x3 box
    }
    return true;
}

bool solve(char** board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char c = '1'; c <= '9'; c++) {
                    if (is_valid(board, i, j, c)) {
                        board[i][j] = c; // place c for this cell

                        if (solve(board))
                            return true; // sudoku solved
                        else
                            board[i][j] = '.'; // undo the choice for this cell
                    }
                }
                return false; // no solution for this cell, backtrack
            }
        }
    }
    return true; // sudoku solved
}

void solveSudoku(char** board, int boardSize, int* boardColSize){
    solve(board);
}

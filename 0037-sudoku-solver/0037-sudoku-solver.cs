public class Solution {
    public void SolveSudoku(char[][] board) {
        solve(board);
    }

    private bool solve(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c; // place number

                            if (solve(board)) {
                                return true; // solve the rest of the grid
                            }

                            board[i][j] = '.'; // undo number placement, backtrack
                        }
                    }
                    return false; // no valid numbers can be placed in this cell
                }
            }
        }
        return true; // all cells are filled
    }

    private bool isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            // check row
            if (board[i][col] == c) {
                return false;
            }
            // check column
            if (board[row][i] == c) {
                return false;
            }
            // check 3x3 box
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) {
                return false;
            }
        }
        return true;
    }
}
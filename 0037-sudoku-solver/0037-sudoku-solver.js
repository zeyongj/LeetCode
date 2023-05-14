/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    function is_valid(board, row, col, num) {
        for (let i = 0; i < 9; i++) {
            const m = 3 * Math.floor(row / 3) + Math.floor(i / 3);
            const n = 3 * Math.floor(col / 3) + i % 3;
            if (board[row][i] == num || board[i][col] == num || board[m][n] == num) {
                return false; // not a valid number
            }
        }
        return true; // number is valid
    }

    function solve(board) {
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (let num = 1; num <= 9; num++) {
                        if (is_valid(board, i, j, String(num))) {
                            board[i][j] = String(num);
                            if (solve(board)) {
                                return true; // solve the rest of the board
                            }
                            board[i][j] = '.'; // undo the current cell for backtracking
                        }
                    }
                    return false; // no valid number can be placed at this cell
                }
            }
        }
        return true; // entire board is solved
    }

    solve(board); // invoke the solve function
};

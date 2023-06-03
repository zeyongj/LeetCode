/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    const board = new Array(n).fill().map(() => new Array(n).fill('.'));
    const res = [];

    const isValid = (row, col) => {
        for(let i = 0; i < row; i++){
            if(board[i][col] === 'Q') {
                return false;
            }
        }

        for(let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--){
            if(board[i][j] === 'Q') {
                return false;
            }
        }

        for(let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++){
            if(board[i][j] === 'Q') {
                return false;
            }
        }

        return true;
    };

    const backtrack = (row) => {
        if(row === n) {
            res.push(board.map(cur => cur.join('')));
            return;
        }

        for(let col = 0; col < n; col++) {
            if(isValid(row, col)) {
                board[row][col] = 'Q';
                backtrack(row + 1);
                board[row][col] = '.';
            }
        }
    };

    backtrack(0);
    return res;
};

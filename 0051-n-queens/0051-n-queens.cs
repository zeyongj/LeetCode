public class Solution {
    private List<IList<string>> result;
    private char[][] board;
    private bool[] colUsed;
    private bool[] diagonals45Used;
    private bool[] diagonals135Used;
    private int n;
    
    public IList<IList<string>> SolveNQueens(int n) {
        this.n = n;
        result = new List<IList<string>>();
        colUsed = new bool[n];
        diagonals45Used = new bool[2 * n - 1]; // diagonals \
        diagonals135Used = new bool[2 * n - 1]; // diagonals /
        board = new char[n][];
        for (int i = 0; i < n; i++) {
            board[i] = new char[n];
            for (int j = 0; j < n; j++) {
                board[i][j] = '.';
            }
        }

        Backtrack(0);
        return result;
    }

    private void Backtrack(int row) {
        if (row == n) {
            List<string> list = new List<string>();
            for (int i = 0; i < n; i++) {
                list.Add(new string(board[i]));
            }
            result.Add(list);
            return;
        }

        for (int col = 0; col < n; col++) {
            int diagonals45Index = row + col;
            int diagonals135Index = n - 1 - (row - col);
            if (colUsed[col] || diagonals45Used[diagonals45Index] || diagonals135Used[diagonals135Index])
                continue;

            board[row][col] = 'Q';
            colUsed[col] = diagonals45Used[diagonals45Index] = diagonals135Used[diagonals135Index] = true;
            Backtrack(row + 1);
            board[row][col] = '.';
            colUsed[col] = diagonals45Used[diagonals45Index] = diagonals135Used[diagonals135Index] = false;
        }
    }
}

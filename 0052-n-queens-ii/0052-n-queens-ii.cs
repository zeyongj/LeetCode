public class Solution {
    int count = 0;
    public int TotalNQueens(int n) {
        int[] board = new int[n];
        Solve(board, 0, n);
        return count;
    }
    
    private void Solve(int[] board, int row, int n) {
        if(row == n) {
            count++;
            return;
        }
        
        for(int col = 0; col < n; col++) {
            if (IsSafe(board, row, col)) {
                board[row] = col;
                Solve(board, row + 1, n);
            }
        }
    }
    
    private bool IsSafe(int[] board, int row, int col) {
        for(int i = 0; i < row; i++) {
            if(board[i] == col) {
                return false;
            }
            if(Math.Abs(board[i] - col) == Math.Abs(i - row)) {
                return false;
            }
        }
        return true;
    }
}

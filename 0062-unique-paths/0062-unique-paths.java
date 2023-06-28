public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];
        
        // Initialize the left column and the top row to 1.
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }

        // For each cell, compute the number of unique paths to reach it
        // by adding the number of paths to reach the cell above it and the cell on its left.
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        // The bottom right cell contains the number of unique paths to reach it.
        return dp[m - 1][n - 1];
    }
}

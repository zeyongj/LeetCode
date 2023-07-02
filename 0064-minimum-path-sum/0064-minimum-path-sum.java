public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        // Initialize the dynamic programming table with the size of grid
        int[][] dp = new int[m][n];

        // Initialize the top left cell
        dp[0][0] = grid[0][0];

        // Calculate the minimum path sum for the first row
        for (int j = 1; j < n; ++j) {
            dp[0][j] = dp[0][j-1] + grid[0][j];
        }

        // Calculate the minimum path sum for the first column
        for (int i = 1; i < m; ++i) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }

        // Calculate the minimum path sum for each remaining cell
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }

        // Return the minimum path sum to reach the bottom right cell
        return dp[m-1][n-1];
    }
}

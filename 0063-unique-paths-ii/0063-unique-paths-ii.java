class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        long[][] dp = new long[m][n];

        if (obstacleGrid[0][0] == 0) dp[0][0] = 1;

        // Handle first row
        for (int j = 1; j < n; j++) {
            if (obstacleGrid[0][j] == 0)
                dp[0][j] = dp[0][j - 1];
        }

        // Handle first column
        for (int i = 1; i < m; i++) {
            if (obstacleGrid[i][0] == 0)
                dp[i][0] = dp[i - 1][0];
        }

        // For the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 0)
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return (int)dp[m - 1][n - 1];
    }
}

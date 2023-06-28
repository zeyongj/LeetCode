class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 1)); // initialize all cells to 1

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // Each cell can be reached either from the cell above it or the cell on its left.
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        // The bottom right cell contains the number of unique paths to reach it.
        return dp[m - 1][n - 1];
    }
};

class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Initialize the dynamic programming table with the size of grid
        dp = [[0]*n for _ in range(m)]

        # Initialize the top left cell
        dp[0][0] = grid[0][0]

        # Calculate the minimum path sum for the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Calculate the minimum path sum for the first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Calculate the minimum path sum for each remaining cell
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        # Return the minimum path sum to reach the bottom right cell
        return dp[-1][-1]

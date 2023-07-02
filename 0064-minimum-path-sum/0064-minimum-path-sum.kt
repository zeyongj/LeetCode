class Solution {
  fun minPathSum(grid: Array<IntArray>): Int {
    val dp = IntArray(grid[0].size)
    dp[0] = grid[0][0]
    for (i in 1 until dp.size)
      dp[i] = dp[i - 1] + grid[0][i]
    
    for (r in 1 until grid.size) {
      dp[0] += grid[r][0]
      for (j in 1 until dp.size)
        dp[j] = minOf(dp[j], dp[j - 1]) + grid[r][j]
    }    
    return dp[dp.size - 1]
  }
}
class Solution {
    fun uniquePathsWithObstacles(obstacleGrid: Array<IntArray>): Int {
        val m = obstacleGrid.size
        val n = obstacleGrid[0].size
        val matrix = Array(m) { IntArray(n) }
        for (i in m - 1 downTo 0)
            for (j in n - 1 downTo 0) {
                matrix[i][j] = when {
                    obstacleGrid[i][j] == 1 -> 0
                    i == m - 1 && j == n - 1 -> 1
                    i == m - 1 -> matrix[i][j + 1]
                    j == n - 1 -> matrix[i + 1][j]
                    else -> matrix[i + 1][j] + matrix[i][j + 1]
                }
            }
        return matrix[0][0]
    }
}
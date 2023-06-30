func uniquePathsWithObstacles(obstacleGrid [][]int) int {
    if obstacleGrid[0][0] == 1 {
        return 0
    }
    x := 1
    for i := range obstacleGrid {
        if obstacleGrid[i][0] == 1 {
            x = 0
        }
        obstacleGrid[i][0] = x
    }
    x = 1
    for i := 1; i < len(obstacleGrid[0]); i++ {
        if obstacleGrid[0][i] == 1 {
            x = 0
        }
        obstacleGrid[0][i] = x
    }
    for i := 1; i < len(obstacleGrid); i++ {
        for j := 1; j < len(obstacleGrid[0]); j++ {
            if obstacleGrid[i][j] == 1 {
                obstacleGrid[i][j] = 0
                continue
            }
            obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        }
    }
    return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
}
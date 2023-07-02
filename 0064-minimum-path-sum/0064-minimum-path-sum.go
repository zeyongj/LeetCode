func minPathSum(grid [][]int) int {
    for i := len(grid[0])-2; i >= 0; i-- {
        grid[len(grid)-1][i] = grid[len(grid)-1][i] + grid[len(grid)-1][i+1]
    }
    for i := len(grid)-2; i >= 0; i-- {
        grid[i][len(grid[0])-1] = grid[i][len(grid[0])-1] + grid[i+1][len(grid[0])-1]
    }
    for i := len(grid)-2; i >= 0; i-- {
        for j := len(grid[0])-2; j >= 0; j-- {
            min := grid[i+1][j]
            if grid[i][j+1] < min {
                min = grid[i][j+1] 
            }
            grid[i][j] = grid[i][j] + min
        }
    }
    return grid[0][0]
}
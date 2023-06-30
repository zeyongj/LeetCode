/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    let m = obstacleGrid[0].length
    let board = new Array(m).fill(0)
    board[0] = 1
    for (let row of obstacleGrid) {
        for (let c = 0; c < m; c++) {
            if (row[c]) {
                board[c] = 0
            } else if (c > 0) {
                board[c] += board[c - 1]
            }  
        }
    }
    return board[m - 1]
};
class Solution {
    func minPathSum(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var cost = Array(repeating:Array(repeating:0,count:n),count:m)
        cost[0][0] = grid[0][0]
		
        //populating the first col 
        for i in 1..<m {
            cost[i][0] = cost[i-1][0] + grid[i][0]
        }
        
        //populating first row
        for i in 1..<n {
            cost[0][i] = cost[0][i-1] + grid[0][i]
        }
        
        for i in 1..<m {
            for j in 1..<n {
                cost[i][j] = grid[i][j] + min(cost[i-1][j], cost[i][j-1])
            }
         }
        return cost[m-1][n-1]
    }
}
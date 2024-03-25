class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]
            
        i = 1
        
        while i < m:
            j = 1
            while j < n:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                j += 1
            i += 1
        
        return grid[m-1][n-1]
        
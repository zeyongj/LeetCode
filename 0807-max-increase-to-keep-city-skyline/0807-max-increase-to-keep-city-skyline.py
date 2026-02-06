class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        row_max = [0] * m
        col_max = [0] * n

        for i in range(m):
            row_max[i] = max(grid[i])
        
        for j in range(n):
            col = 0 
            for i in range(m):
                col = max(col, grid[i][j])
            col_max[j] = col
        
        for i in range(m):
            for j in range(n):
                res += min(row_max[i], col_max[j]) - grid[i][j]
        return res
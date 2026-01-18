class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 2 or m < 2:
            return 1

        row_prefix = [[0]*(m+1) for _ in range(n)]
        col_prefix = [[0]*(m) for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                row_prefix[i][j+1] = row_prefix[i][j] + grid[i][j]
        
        for j in range(m):
            for i in range(n):
                col_prefix[i+1][j] = col_prefix[i][j] + grid[i][j]
        
        for k in range(min(n, m), 1, -1):
            for r in range(n - k + 1):
                for c in range(m - k + 1):
                        
                    target = row_prefix[r][c+k] - row_prefix[r][c]
                        
                    magic = True
                        
                    for i in range(k):
                        row_sum = row_prefix[r+i][c+k] - row_prefix[r+i][c]
                        if row_sum != target:
                            magic = False
                            break
                    if not magic: 
                        continue

                    for j in range(k):
                        col_sum = col_prefix[r+k][c+j] - col_prefix[r][c+j]
                        if col_sum != target:
                            magic = False
                            break
                    if not magic: 
                        continue
                            
                    d1, d2 = 0, 0
                    for i in range(k):
                        d1 += grid[r+i][c+i]
                        d2 += grid[r+i][c+k-1-i]
                            
                    if d1 == target and d2 == target:
                        return k
        return 1
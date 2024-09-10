class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = list(map(sum, grid))
        cols = list(map(sum, zip(*grid)))
        
        res = 0
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                res += 1

        return res
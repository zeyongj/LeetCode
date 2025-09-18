class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_counts = [0] * rows
        col_counts = [0] * cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        triangles = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    triangles += (row_counts[r] - 1) * (col_counts[c] - 1)

        return triangles
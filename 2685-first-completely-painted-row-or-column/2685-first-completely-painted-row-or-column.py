class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        position_map = {mat[r][c]: (r, c) for r in range(rows) for c in range(cols)}
        row_count = [cols] * rows
        col_count = [rows] * cols
        for idx, val in enumerate(arr):
            row, col = position_map[val]
            row_count[row] -= 1
            col_count[col] -= 1
            if row_count[row] == 0 or col_count[col] == 0:
                return idx
        return -1
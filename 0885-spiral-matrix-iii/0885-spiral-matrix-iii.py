class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [0, 1, 0, -1, 0]
        res = [[rStart, cStart]]
        j = n = 0
        while len(res) < rows * cols:
            for i in range(n // 2 + 1):
                rStart += directions[j]
                cStart += directions[j + 1]
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    res.append([rStart, cStart])
            n += 1
            j = (j + 1) % 4
        return res
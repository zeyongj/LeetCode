class Solution:
    def generateMatrix(self, n):
        matrix = [[0]*n for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, n-1, 0, n-1

        while True:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1
            if top > bottom: break

            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            if left > right: break

            for i in range(right, left-1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            if top > bottom: break

            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
            if left > right: break

        return matrix

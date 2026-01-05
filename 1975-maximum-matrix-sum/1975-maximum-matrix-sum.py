class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_val = 0
        c = 0
        mini = float('inf')
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                sum_val += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    c += 1
                mini = min(mini, abs(matrix[i][j]))
        
        if c % 2 == 1:
            sum_val -= 2 * mini
        
        return sum_val
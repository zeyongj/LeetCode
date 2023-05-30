class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        
        # Reverse each row
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]

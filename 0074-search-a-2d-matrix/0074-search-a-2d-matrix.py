class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        size = row * col
        
        if size == 0:
            return False
        
        start = 0
        end = size - 1
        
        while (start + 1 < end):
            mid = (start + end) // 2
            mid_x = mid // col
            mid_y = mid % col
            if (matrix[mid_x][mid_y] < target):
                start = mid
            else:
                end = mid
        
        start_x = start // col
        start_y = start % col
        end_x = end // col
        end_y = end % col
        
        if matrix[start_x][start_y] == target or matrix[end_x][end_y] == target:
            return True
        else:
            return False
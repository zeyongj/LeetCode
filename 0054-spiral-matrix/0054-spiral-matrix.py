from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            # add the first row to result
            result += matrix.pop(0)
            # rotate the matrix counter-clockwise
            matrix = list(zip(*matrix))[::-1]
        return result

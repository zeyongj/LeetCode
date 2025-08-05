class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}
        # every value in a diagonal has the same y - x value
        for y in range(len(mat)): 
            for x in range(len(mat[0])): 
                index = y - x 
                if index in diagonals: 
                    diagonals[index].append(mat[y][x])
                else: 
                    diagonals[index] = [mat[y][x]]

        # sorts in descending order, so values can pop quickly
        for key in diagonals: 
            diagonals[key] = sorted(diagonals[key], reverse=True)

        for y in range(len(mat)): 
            for x in range(len(mat[0])): 
                index = y - x
                mat[y][x] = diagonals[index].pop()

        return mat
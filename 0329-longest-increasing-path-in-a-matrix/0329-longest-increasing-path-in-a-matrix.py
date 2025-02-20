class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #Initialize ROWS, COLS to len(matrix), len(matrix[0]) respectively
        ROWS, COLS = len(matrix), len(matrix[0])

        #Initialize a dp hashmap to cache values 
        dp = {}

        #Create a dfs() helper function taking r, c, prevVal as parameters
        def dfs(r, c, prevVal):
            #Check if r, c is out of bounds ot prevVal >= matrix[r][c]
            if (r < 0 or r == ROWS or c < 0 or c == COLS or prevVal >= matrix[r][c]):
                #return 0
                return 0
            #Check if (r, c) is already in dp
            if (r, c) in dp:
                #Return dp[(r, c)]
                return dp[(r, c)]

            #Initialize res to 1
            res = 1
            #Update res to max(res, the neighbouring coordinates of r, c by passing them to recursive dfs() calls and passing matrix[r][c] as prevVal parameter.
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            #Initialize dp[(r, c)] to res
            dp[(r, c)] = res
            #return res
            return res

        #Iterate for r in range(ROWS)
        for r in range(ROWS):
            #Iterate for c in range(COLS)
            for c in range(COLS):
                #Call dfs() passing r, c and -1. -1 is the default prevVal  
                dfs(r, c, -1)

        #Return max(dp.values())
        return max(dp.values())
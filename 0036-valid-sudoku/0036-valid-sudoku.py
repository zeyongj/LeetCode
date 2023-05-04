class Solution:
    def isValidSudoku(self, board):
        seen = set()
        
        for i in range(9):
            for j in range(9):
                number = board[i][j]
                if number != '.':
                    row = "{} seen in row {}".format(number, i)
                    col = "{} seen in col {}".format(number, j)
                    box = "{} seen in box {}-{}".format(number, i // 3, j // 3)

                    if (row in seen) or (col in seen) or (box in seen):
                        return False

                    seen.add(row)
                    seen.add(col)
                    seen.add(box)

        return True

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]
        for i in range(1, numRows):
            a += [list(map(lambda x, y: x+y, a[-1] + [0], [0] + a[-1]))]
        return a[:numRows]
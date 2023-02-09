class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = []
        n = len(s)
        cycleLen = 2 * numRows - 2
        
        for i in range(numRows):
            for j in range(0, n, cycleLen):
                if j + i < n:
                    res.append(s[j + i])
                if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                    res.append(s[j + cycleLen - i])
        
        return ''.join(res)

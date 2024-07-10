class Solution(object):
    def sumZero(self, n):
        res = []
        for i in range(1, n//2 + 1):
            res.append(i)
            res.append(-i)
        if n % 2 != 0:
            res.append(0)
        return res
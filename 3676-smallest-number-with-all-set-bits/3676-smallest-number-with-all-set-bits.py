class Solution(object):
    def smallestNumber(self, n):
        for i in range(n + 1):
            z = 1 << i
            if z > n:
                return z - 1
        return 0
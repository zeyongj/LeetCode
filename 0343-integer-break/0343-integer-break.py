class Solution:
    def integerBreak(self, n: int) -> int:
        if(n <= 3):
            return n-1
        n3 = n // 3
        r3 = n % 3
        if(r3 == 0):
            return 3 ** n3
        if(r3 == 1):
            r3 = 4
            n3 -= 1
        return r3*(3 ** n3)
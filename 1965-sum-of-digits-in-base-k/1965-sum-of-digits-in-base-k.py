class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = []
        while n>0:
            digits.append(n%k)
            n //= k

        return sum(digits)
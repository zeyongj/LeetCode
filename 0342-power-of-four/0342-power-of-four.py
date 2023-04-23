class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else n == pow(4, round(math.log(n, 4)))
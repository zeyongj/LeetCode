class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else n == pow(3, round(math.log(n, 3)))
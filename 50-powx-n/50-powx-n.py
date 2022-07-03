class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x * x
        ans = self.myPow(x, n >> 1)
        ans = ans * ans
        if n % 2 == 1: ans *= x
        return ans
class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10 ** 9 + 7
        if n < 4:
            return 0

        # total combination:
        ans = pow(26, n, mod)
        
        # l = 0
        sub = (pow(25, n, mod)) % mod
        # t = 0
        sub += (pow(25, n, mod)) % mod
        # e = 0, 1
        sub += (pow(25, n, mod) + n * pow(25, n-1, mod)) % mod
        # l = 0, t = 0
        sub -= pow(24, n, mod)
        # l = 0, e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n-1, mod)) % mod
        # t = 0, e < 2
        sub -= (pow(24, n, mod) + n * pow(24, n-1, mod)) % mod
        # l = 0, t = 0, e < 2
        sub += (pow(23, n, mod) + n * pow(23, n-1, mod)) % mod
        return (ans - sub) % mod
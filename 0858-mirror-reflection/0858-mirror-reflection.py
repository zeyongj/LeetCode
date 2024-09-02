import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        y = q
        x = p
        gcd = math.gcd(y, x)
        y //= gcd
        x //= gcd

        if y % 2 == 0:
            return 0
        else:
            if x % 2 == 1:
                return 1
            else:
                return 2
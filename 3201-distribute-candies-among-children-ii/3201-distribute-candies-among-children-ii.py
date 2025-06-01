class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Computes C(x,2) = x*(x-1)//2, or 0 if x<2
        def C2(x: int) -> int:
            return (x * (x - 1) // 2) if x >= 2 else 0

        total = (n+2)*(n+1)//2 # Count = C(n+2, 2)
        x1 = n - limit + 1     # Count with a > limit 
        t1 = C2(x1)

        x2 = n - 2 * limit     # Count with a > limit
        t2 = C2(x2)            # and b > limit

        x3 = n - 3 * limit - 1 # Count with a > limit
        t3 = C2(x3)            # b > limit, c > limit

        # Inclusion–exclusion
        return total - 3 * t1 + 3 * t2 - t3
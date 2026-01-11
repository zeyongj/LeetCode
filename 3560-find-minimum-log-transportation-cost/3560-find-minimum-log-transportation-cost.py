class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:

        ans = 0

        if m <= k and n <= k:
            return 0

        if m > k and n <= k:
            ans += (m - k) * k
        if n > k and m <= k:
            ans += (n - k) * k


        return ans
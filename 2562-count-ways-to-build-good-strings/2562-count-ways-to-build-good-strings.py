class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = int(1e9 + 7)
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: 1 way to create an empty string

        for i in range(high + 1):
            if dp[i] > 0:
                if i + zero <= high:
                    dp[i + zero] = (dp[i + zero] + dp[i]) % mod
                if i + one <= high:
                    dp[i + one] = (dp[i + one] + dp[i]) % mod

        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % mod
        return result
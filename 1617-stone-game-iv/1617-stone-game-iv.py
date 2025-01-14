class Solution:
    def winnerSquareGame(self, n):
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]
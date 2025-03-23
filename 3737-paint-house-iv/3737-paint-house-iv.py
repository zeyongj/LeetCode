class Solution:
    def __init__(self):
        self.dp = None

    def solve(self, c, l, r, i):
        n = len(c)
        if i >= n // 2:
            return 0

        if self.dp[i][l][r] != -1:
            return self.dp[i][l][r]

        left_choices = [j for j in range(3) if j != l]
        right_choices = [j for j in range(3) if j != r]

        ans = float('inf')

        for h in left_choices:
            for j in right_choices:
                if h == j:
                    continue
                cl = c[i][h]
                cr = c[n - i - 1][j]
                ans = min(ans, cl + cr + self.solve(c, h, j, i + 1))

        self.dp[i][l][r] = ans
        return ans

    def minCost(self, n, c):
        self.dp = [[[-1] * 4 for _ in range(4)] for _ in range(n // 2 + 1)]
        return self.solve(c, 3, 3, 0)
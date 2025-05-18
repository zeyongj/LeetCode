class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
       # Solution 1:
        def dfs(pos, prev_color, mask):
            if pos == m:
                states.append(mask)
                return
            for color in range(3):
                if color != prev_color:
                    dfs(pos + 1, color, mask * 3 + color)

        MOD, states = 10**9 + 7, []
        dfs(0, -1, 0)
        S = len(states)
        compat = [[] for _ in range(S)]
        for i, s1 in enumerate(states):
            for j, s2 in enumerate(states):
                x, y = s1, s2
                ok = True
                for _ in range(m):
                    if x % 3 == y % 3:
                        ok = False
                        break
                    x //= 3
                    y //= 3
                if ok:  compat[i].append(j)
        dp = [1] * S
        for _ in range(n - 1):
            new_dp = [0] * S
            for i in range(S):
                if dp[i]:
                    for j in compat[i]:
                        new_dp[j] = (new_dp[j] + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD 
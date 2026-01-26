class Solution:
    def minOperations(self, S, T):
        N = len(S)
        dp = [inf] * N + [0]

        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                S1 = S[i:j+1]
                T1 = T[i:j+1]

                e1 = Counter(zip(S1, T1))
                m1 = sum(v for (a, b), v in e1.items() if a != b)
                s1 = sum(min(e1[a,b], e1[b,a]) for (a,b) in e1 if a < b)
                dp[i] = min(dp[i], m1 - s1 + dp[j + 1])

                e2 = Counter(zip(S1[::-1], T1))
                m2 = sum(v for (a, b), v in e2.items() if a != b)
                s2 = sum(min(e2[a,b], e2[b,a]) for (a,b) in e2 if a < b)
                dp[i] = min(dp[i], 1 + m2 - s2 + dp[j+1])

        return dp[0]
class Solution:
    def numberOfUniqueGoodSubsequences(self, S):
        dp, last = [1], {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            dp[-1] -= dp[last[x]] if x in last else int(x == "0")
            dp[-1] = dp[-1] % (10**9 + 7)
            last[x] = i

        return dp[-1] - 1 + int("0" in S)
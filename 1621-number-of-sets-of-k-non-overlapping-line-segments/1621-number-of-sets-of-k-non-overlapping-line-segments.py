class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        @lru_cache(None)
        def dp(i, k, isStart):
            if k == 0: return 1 
            if i == n: return 0 
            ans = dp(i+1, k, isStart) 
            if isStart:
                ans += dp(i+1, k, False)
            else:
                ans += dp(i, k-1, True)
            return ans % MOD
        return dp(0, k, True)
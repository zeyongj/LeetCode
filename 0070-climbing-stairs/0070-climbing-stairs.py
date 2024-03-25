class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [1] * (n+1)
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
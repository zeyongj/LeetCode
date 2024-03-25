import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n+1)
        
        dp[0] = 0
        
        for i in range(1, n+1):
            j = 1
            while pow(j,2) <= i:
                dp[i] = min(dp[i], dp[i- pow(j,2)] + 1)
                j += 1
            
        return dp[n]
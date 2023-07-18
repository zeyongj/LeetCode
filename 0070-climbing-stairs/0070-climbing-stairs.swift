class Solution {
 func climbStairs(_ n: Int) -> Int {
        var dp = [1,1]
        if n < 2
        {
            return 1
        }
        if n == 2
        {
            return dp[0] + dp[1]
        }
        
        for i in 2...n
        {
            dp.append(dp[i-1] + dp[i-2])
        }
        
        return dp[n]
    }
}
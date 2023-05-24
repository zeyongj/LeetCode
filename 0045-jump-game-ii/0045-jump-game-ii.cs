public class Solution {
    public int Jump(int[] nums) {
        int n = nums.Length;
        int[] dp = new int[n];
        for(int i = 0; i < n; i++) {
            dp[i] = int.MaxValue;
        }
        dp[n-1] = 0;
        for(int i=n-2; i>=0; i--) {
            int steps = Math.Min(n-1, i + nums[i]);
            for(int j=i+1; j<=steps; j++) {
                if(dp[j] != int.MaxValue) {
                    dp[i] = Math.Min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[0];        
    }
}
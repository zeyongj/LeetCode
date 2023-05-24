class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        for(int i = 0; i < n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        dp[n-1] = 0;
        for(int i=n-2; i>=0; i--) {
            int steps = Math.min(n-1, i + nums[i]);
            for(int j=i+1; j<=steps; j++) {
                if(dp[j] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[0];
    }
}

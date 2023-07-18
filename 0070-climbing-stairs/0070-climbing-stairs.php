impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![1,2];
        
        for i in 2..n {
            dp.push(
                dp[i - 1] + dp[i - 2]
            );
        }
        
        dp[n - 1]
    }
}
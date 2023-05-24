impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut dp = vec![std::i32::MAX; n];
        dp[n-1] = 0;
        for i in (0..n-1).rev() {
            let steps = std::cmp::min(n-1, i + nums[i] as usize);
            for j in (i+1..=steps) {
                if dp[j] != std::i32::MAX {
                    dp[i] = std::cmp::min(dp[i], dp[j] + 1);
                }
            }
        }
        dp[0]
    }
}

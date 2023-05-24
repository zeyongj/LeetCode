func jump(nums []int) int {
    n := len(nums)
    dp := make([]int, n)
    for i := 0; i < n; i++ {
        dp[i] = 1<<31 - 1 // equivalent to INT_MAX in Go
    }
    dp[n-1] = 0
    for i := n - 2; i >= 0; i-- {
        steps := min(n-1, i + nums[i])
        for j := i + 1; j <= steps; j++ {
            if dp[j] != 1<<31 - 1 {
                dp[i] = min(dp[i], dp[j] + 1)
            }
        }
    }
    return dp[0]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

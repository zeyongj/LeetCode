class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [float('inf')] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            steps = min(n-1, i + nums[i])
            for j in range(i+1, steps+1):
                if dp[j] != float('inf'):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]

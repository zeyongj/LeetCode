class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0 for i in range(k + 1)] for i in range(len(nums))]
        max_dp, prev = [0] * (k + 1), {}
        for i in range(len(nums) - 1, -1, -1):
            p = prev[nums[i]] if nums[i] in prev else 0
            for j in range(k, -1, -1):
                dp[i][j] = 1 + max(dp[p][j], max_dp[j - 1] if j else 0)
                max_dp[j] = max(max_dp[j], dp[i][j])
            prev[nums[i]] = i
        return max(dp[i][k] for i in range(len(nums)))
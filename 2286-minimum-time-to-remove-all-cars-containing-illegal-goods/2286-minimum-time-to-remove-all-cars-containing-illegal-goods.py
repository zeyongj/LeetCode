class Solution:
    def minimumTime(self, s):
        def minSum(nums):
            dp, dp_min = nums[0], nums[0]
            for i in range(1, len(nums)):
                dp = min(nums[i], nums[i] + dp)
                dp_min = min(dp, dp_min)
            return min(0, dp_min)
        return len(s) + minSum([1 if i == "1" else -1 for i in s])
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        max_value = max(nums)
        if all(n < 0 for n in nums):
            return max_value

        seen = [False] * 101
        for n in nums:
            if 0 <= n <= 100:
                seen[n] = True

        return sum(i for i, present in enumerate(seen[1:], start=1) if present)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = 0
        min_elem = nums[0]

        for i in nums:
            max_diff = max(max_diff, i - min_elem)
            min_elem = min(min_elem, i)

        return max_diff if max_diff > 0 else -1
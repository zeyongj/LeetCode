class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[0]-nums[-1]), max(abs(x-y) for x, y in pairwise(nums)))
        
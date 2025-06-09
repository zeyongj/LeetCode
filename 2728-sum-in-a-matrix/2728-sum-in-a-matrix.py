class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        return sum(max(col) for col in zip(*[sorted(row) for row in nums]))
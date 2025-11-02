class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        rest = [x%3 for x in nums if x%3 != 0]
        return len(rest)
        
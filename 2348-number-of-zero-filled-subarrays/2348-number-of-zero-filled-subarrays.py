class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        return sum(accumulate(nums, lambda a, x: 0 if x else a + 1, initial=0))

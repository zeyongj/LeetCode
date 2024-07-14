class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        return max(math.ceil(nums.count(reduce(math.gcd, nums)) / 2), 1)
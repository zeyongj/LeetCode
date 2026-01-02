class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        return sum(1 for i in nums if mn < i < mx)
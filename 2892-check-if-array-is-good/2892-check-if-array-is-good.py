class Solution:
    def isGood(self, nums):
        max_num = max(nums)
        return sorted(nums) == list(range(1, max_num+1)) + [max_num]
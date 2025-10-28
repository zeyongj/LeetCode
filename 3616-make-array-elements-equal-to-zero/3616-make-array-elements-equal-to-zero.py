class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        left = 0
        right = sum(nums)
        for i in range(length):
            left += nums[i]
            right -= nums[i]
            if nums[i] != 0: continue
            if left == right: count += 2
            if abs(left - right) == 1: count += 1
        return count

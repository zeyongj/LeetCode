class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        min_increments = 0
        size = len(nums)

        nums.sort()

        for i in range(1, size):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] + 1 - nums[i]
                min_increments += increment
                nums[i] = nums[i - 1] + 1

        return min_increments
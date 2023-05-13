class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        # First, we segregate positive numbers and non-positive numbers.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        # Then, we find the first index where the index+1 doesn't match the number at that index
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1  # As the array is 0-indexed, the first missing positive is i+1
        
        # If all indices matched, then the first missing positive is the array size+1
        return n + 1

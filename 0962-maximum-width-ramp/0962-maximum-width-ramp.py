class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        rightMax = [0] * n
        rightMax[n - 1] = nums[n - 1]

        # Fill the rightMax array
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i])

        left, right, maxVal = 0, 0, 0

        # Find the maximum width ramp
        while right < n:
            while right < n and nums[left] <= rightMax[right]:
                right += 1
            
            maxVal = max(maxVal, right - left - 1)
            left += 1
            right = left + maxVal + 1

        return maxVal
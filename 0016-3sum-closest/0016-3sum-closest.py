from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(target - closest_sum)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum_)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum_

                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    return target  # The sum is equal to the target, so it's the closest.

        return closest_sum
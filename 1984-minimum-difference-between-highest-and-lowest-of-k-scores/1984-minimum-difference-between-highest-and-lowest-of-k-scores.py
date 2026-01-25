mn = lambda x, y: x if x < y else y

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        nums.sort()
        ans = inf

        for lft, rgt in zip(nums, nums[k-1:]):
            ans = mn(ans, rgt - lft)

        return ans 
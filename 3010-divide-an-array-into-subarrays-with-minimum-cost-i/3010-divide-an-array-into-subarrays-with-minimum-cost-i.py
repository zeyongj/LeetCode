class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums[1:] = sorted(nums[1:])
        ans += nums[1]
        ans += nums[2]
        return ans
 

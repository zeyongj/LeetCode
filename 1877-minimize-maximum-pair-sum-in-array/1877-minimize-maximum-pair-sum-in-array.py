from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_pair_sum = 0
        n = len(nums)
        
        for i in range(n // 2):
            pair_sum = nums[i] + nums[n - 1 - i]
            max_pair_sum = max(max_pair_sum, pair_sum)
        
        return max_pair_sum

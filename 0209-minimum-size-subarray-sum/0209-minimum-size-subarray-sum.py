import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        
        if size == 0:
            return 0
        
        left = 0
        right = 0
        total = 0
        
        result = math.inf
        
        while (right < size):
            total += nums[right]
            right += 1
            while (total >= target):
                result = min(result, right-left)
                total -= nums[left]
                left += 1 # When leaving the loop, total < s, i.e. need next right
        
        if result > size:
            return 0
        else:
            return result
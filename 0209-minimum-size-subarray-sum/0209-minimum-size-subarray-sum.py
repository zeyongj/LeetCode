class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, right = 0, 0
        _sum = 0
        min_len = float('inf')
        
        while right < len(nums):
            _sum += nums[right]
            
            while _sum >= target:
                min_len = min(min_len, right - left + 1)
                _sum -= nums[left]
                left += 1
            right += 1
            
        return min_len if min_len != float('inf') else 0

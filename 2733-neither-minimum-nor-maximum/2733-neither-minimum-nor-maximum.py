class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        max_val, min_val = max(nums), min(nums)
        
        nums_set = set(nums)
        
        nums_set.discard(max_val)
        nums_set.discard(min_val)
        
        if len(nums_set) == 0:
            return -1
        else:
            return nums_set.pop()

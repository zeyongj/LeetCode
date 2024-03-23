class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        
        if size == 0:
            return -1
        
        start = 0
        end = size - 1
        
        while (start + 1 < end):
            mid = (start + end) // 2
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
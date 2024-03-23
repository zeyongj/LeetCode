class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        
        if size == 0:
            return -1
        
        start = 0
        end = size - 1
        
        while(start+1 < end):
            mid = (start + end) // 2
            
            if (nums[mid] < nums[mid+1]):
                start = mid
            else:
                end = mid
        
        if nums[start] < nums[end]:
            return end
        else:
            return start
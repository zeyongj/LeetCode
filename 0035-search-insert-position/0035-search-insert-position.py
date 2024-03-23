class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        size = len(nums)
        
        left = 0
        right = size - 1
        
        while(left + 1 < right):
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid
            
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        
        if (nums[left] < target < nums[right]):
            return right
        elif (target < nums[left]):
            return left
        else:
            return right+1
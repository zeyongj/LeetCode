class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find_min_max(l, r):
            local_minimum = float('inf')
            local_maximum = float('-inf')
            for i in range(l, r+1):
                if i == len(nums):
                    break
                local_minimum = min(local_minimum, nums[i])
                local_maximum = max(local_maximum, nums[i])
                
            return local_minimum, local_maximum
                
        if len(nums) < 2: return 0
        
        l, r = 0, len(nums) - 1
        
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        
        while r > 0 and nums[r] >= nums[r -1]:
            r -= 1
            
        if l > r:
            return 0
            
        tempMin, tempMax = find_min_max(l, r+1)
        
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1
            
        return r - l + 1
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        size = len(nums)
        
        if (size == 0):
            return 0
        
        current_count = 0
        max_count = 0
        
        for i in range(size):
            if (nums[i] == 1):
                current_count += 1
            else:
                max_count = max(current_count, max_count)
                current_count = 0
        
        return max(current_count, max_count) #In case the last element is 1
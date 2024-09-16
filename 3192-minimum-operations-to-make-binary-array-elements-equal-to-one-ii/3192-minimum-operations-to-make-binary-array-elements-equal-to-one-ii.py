class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        res = 0
        zero_found = False
        
        for i in range(len(nums)):
            if nums[i] == 0 and zero_found == False:
                zero_found = True
            elif nums[i] == 1 and zero_found == True:
                res += 2
                zero_found = False

        if nums[-1] == 0:
            res += 1
            
        return res    
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        summ = nums[0]
        idx = 1
        while idx<len(nums) and nums[idx] == nums[idx-1]+1:
            summ+=nums[idx]
            idx+=1
        while summ in num_set:
            summ+=1
        
        return summ
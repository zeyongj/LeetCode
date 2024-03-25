class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_map = {}
        
        n = len(nums)
        
        for num in nums:
            if num not in num_map.keys():
                num_map[num] = 1
            else:
                num_map[num] += 1
                
        for key,value in num_map.items():
            if value > n/2:
                return key
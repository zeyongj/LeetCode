class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        
        for num in nums:
            if num in mapping:
                mapping[num] += 1
            else:
                mapping[num] = 1
        
        for key, val in mapping.items():
            if val == 1:
                return key
        
        return -1
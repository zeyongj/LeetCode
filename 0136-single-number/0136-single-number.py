class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        
        for num in nums:
            if num in mapping.keys():
                mapping[num] += 1
            else:
                mapping[num] = 1
        
        for num, occur in mapping.items():
            if occur == 1:
                return num
                
        
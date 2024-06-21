class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num_dict = {}
        
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        
        for key,value in num_dict.items():
            if value > 2:
                return False
        
        return True
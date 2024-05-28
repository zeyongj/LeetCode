class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {} 
        
        for i, num in enumerate(nums):
            if num in num_dict and abs(i - num_dict[num]) <= k:
                return True
            num_dict[num] = i  # Update the index of the current element
            
        return False

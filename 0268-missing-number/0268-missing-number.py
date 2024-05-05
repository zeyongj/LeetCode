class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        length = len(s)
        
        for num in range(length + 1):
            if num not in s:
                return num
        
        
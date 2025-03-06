class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r|=n
        
        return r
        
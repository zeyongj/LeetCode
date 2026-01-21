class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        return [ p^((remB:=((p+1)& -(p+1))>>1)|(-(remB==0) & ~p)) for p in nums]
        
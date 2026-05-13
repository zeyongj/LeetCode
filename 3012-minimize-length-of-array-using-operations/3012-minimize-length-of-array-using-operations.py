class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
        gcd_ = gcd(*nums)
        
        ans = (nums.count(gcd_)+1)//2
        
        return ans if ans else 1
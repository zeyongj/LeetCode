from math import gcd
class Solution:
    
    def lcm(self,a, b):
        return abs(a*b) // math.gcd(a, b)

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        size = len(nums)
        for ind in range(size) :

            curLcm  = nums[ind]

            for ind2 in range(ind, size) :
                curLcm = self.lcm(curLcm, nums[ind2])
                cnt += (curLcm  == k)

        return cnt
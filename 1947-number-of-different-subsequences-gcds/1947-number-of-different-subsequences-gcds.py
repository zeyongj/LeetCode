class Solution:
    def countDifferentSubsequenceGCDs(self, nums):
        T = max(nums) + 1
        nums = set(nums)
        ans = 0
            
        for x in range(1, T):
            g = 0
            for y in range(x, T, x):
                if y in nums:
                    g = gcd(g, y)
                if g == x:
                    break
                    
            if g == x: ans += 1
                
        return ans
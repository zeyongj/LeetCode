class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 1
        
        min_val = min(a,b)
        
        for num in range(2, min_val + 1):
            if a % num == 0 and b % num == 0:
                count += 1
        
        return count
class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        sm = (n+1)*n//2 %1_000_000_007

        if target >= 2*n:  return sm 
      
        sm+= (n - target//2) * ((target-1)//2)
        
        return sm %1_000_000_007
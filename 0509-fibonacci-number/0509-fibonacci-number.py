class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        sum = self.fib(n-1) + self.fib(n-2)
        
        return sum
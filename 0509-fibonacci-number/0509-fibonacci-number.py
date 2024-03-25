class Solution:
    # Dynamic Programming:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]
    
#     # Memorization Mechanism
#     def __init__(self):
#         self.memo = {}
    
#     def fib(self, n: int) -> int:
#         if n < 2 :
#             self.memo[n] = n
        
#         if n in self.memo.keys():
#             return self.memo[n]
#         else:
#             self.memo[n] = self.fib(n-1) + self.fib(n-2) # # Use self to refer to the current instance of the class.
        
#         return self.memo[n]
    
    # Brutal Force:
#     def fib(self, n: int) -> int:
#         if n < 2 :
#             return n
        
#         sum = self.fib(n-1) + self.fib(n-2) # # Use self to refer to the current instance of the class.
        
#         return sum
    
    
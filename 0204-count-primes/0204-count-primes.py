class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # Initialize a list to track prime status of numbers less than n
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False 
        
        # Use the Sieve of Eratosthenes algorithm
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count the number of primes
        return sum(is_prime)

# from sympy import primepi

# class Solution:
#     def countPrimes(self, n: int) -> int:
#         return primepi(n)
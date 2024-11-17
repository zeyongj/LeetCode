class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_prime_factors(n):
            sum_pf = 0
            temp_n = n
            i = 2
            while i * i <= n:
                while n % i == 0:
                    sum_pf += i
                    n //= i
                i += 1
            if n > 1:
                sum_pf += n
            return sum_pf

        while True:
            n_new = sum_prime_factors(n)
            if n_new == n:
                break
            n = n_new
        return n

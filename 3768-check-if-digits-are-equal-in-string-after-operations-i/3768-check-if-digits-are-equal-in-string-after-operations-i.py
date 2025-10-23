class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(digits) for digits in s]
        n = len(s)
        binomial_coeff = [1] * (n - 1)
        # recursive definition of the coefficients
        for i in range(1, n - 1):
            binomial_coeff[i] = binomial_coeff[i-1] * (n-2-i+1) // i
        
        left = sum([digit*coeff for digit, coeff in zip(s[:-1], binomial_coeff)]) % 10
        right = sum([digit*coeff for digit, coeff in zip(s[1:], binomial_coeff)]) % 10
        return left == right
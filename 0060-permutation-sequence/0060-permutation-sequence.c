class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        numbers = list(range(1, n+1))
        k -= 1
        permutation = ''
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            permutation += str(numbers.pop(index))
        return permutation
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def permutation(m, k):
            # Computes the number of ways to arrange k numbers out of m possibilities.
            result = 1
            for i in range(k):
                result *= (m - i)
            return result

        s = str(N)
        n = len(s)
        # Count unique-digit numbers with fewer digits than N.
        unique_count = 0
        for i in range(1, n):
            unique_count += 9 * permutation(9, i - 1)
        
        # Count unique-digit numbers with the same number of digits as N.
        seen = set()
        for i, char in enumerate(s):
            digit = int(char)
            # For each digit position, consider smaller digits not used so far.
            for j in range(0 if i > 0 else 1, digit):
                if j in seen:
                    continue
                unique_count += permutation(10 - i - 1, n - i - 1)
            # If the current digit is already used, break out.
            if digit in seen:
                break
            seen.add(digit)
        else:
            # If loop completes without break, include N itself.
            unique_count += 1

        # Total numbers (0 to N) minus unique-digit numbers gives the duplicate-digit count.
        return N - unique_count
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0  # \U0001f35c Mission count

        for num in range(low, high + 1):
            s = str(num)  # \U0001f50d Naruto's string transformation no jutsu
            n = len(s)

            if n % 2 != 0:
                continue  # ☠️ Odd-digit numbers are not balanced, skip

            half = n // 2
            left = sum(int(s[i]) for i in range(half))  # ⬅️ Left chakra
            right = sum(int(s[i]) for i in range(half, n))  # ➡️ Right chakra

            if left == right:
                count += 1  # ✅ Symmetry detected, add to mission count

        return count
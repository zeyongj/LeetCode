class Solution:
    def monkeyMove(self, n: int) -> int:
        mod = 10 ** 9 + 7
        return (pow(2, n, mod) + mod - 2) % mod
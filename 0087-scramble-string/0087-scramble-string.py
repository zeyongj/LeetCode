class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        return self.is_scramble_recursive(s1, s2, memo)

    def is_scramble_recursive(self, s1: str, s2: str, memo: dict) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        key = s1 + "_" + s2
        if key in memo:
            return memo[key]

        if sorted(s1) != sorted(s2):
            return False

        n = len(s1)
        for i in range(1, n):
            if (self.is_scramble_recursive(s1[:i], s2[:i], memo) and self.is_scramble_recursive(s1[i:], s2[i:], memo)) or \
               (self.is_scramble_recursive(s1[:i], s2[-i:], memo) and self.is_scramble_recursive(s1[i:], s2[:-i], memo)):
                memo[key] = True
                return True

        memo[key] = False
        return False

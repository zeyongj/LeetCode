class Solution:
    def countOdds(self, a: int, b: int) -> int:
        return ((b - a) >> 1) + ((a | b) & 1)
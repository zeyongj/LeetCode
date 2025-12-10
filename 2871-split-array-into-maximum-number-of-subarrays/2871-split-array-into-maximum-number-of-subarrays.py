class Solution:
    def maxSubarrays(self, A: List[int]) -> int:
        v = -1
        res = 0
        for a in A:
            v &= a
            if v == 0:
                v = -1
                res += 1
        return max(1, res)
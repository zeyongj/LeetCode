class Solution:
    def minCapability(self, A: List[int], k: int) -> int:
        l, r = min(A), max(A)
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in A:
                if last:
                    last = 0
                    continue
                if a <= m:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return l
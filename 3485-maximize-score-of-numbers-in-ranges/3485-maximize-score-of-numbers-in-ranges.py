class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        
        def fn(mid): 
            x = -inf
            for s in start: 
                x += mid
                if x > s+d: return False 
                x = max(x, s)
            return True 
        
        lo, hi = 0, 2_000_000_000
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid-1
        return lo 
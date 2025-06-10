class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        maxOdd, minEven=0, 100
        for f in freq.values():
            if f==0: continue
            if f&1: maxOdd=max(f, maxOdd)
            else: minEven=min(f, minEven)
        return maxOdd-minEven
        
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mp = dict(zip(chars, vals))
        ans = val = 0 
        for i, ch in enumerate(s):
            val = max(0, val + mp.get(ch, ord(ch)-96))
            ans = max(ans, val)
        return ans 
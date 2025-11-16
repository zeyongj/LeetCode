class Solution:
    def numSub(self, s: str) -> int:
       return (cnt:=0) or sum(cnt:=cnt+1 if c=='1' else 0 for c in s)%1000000007      
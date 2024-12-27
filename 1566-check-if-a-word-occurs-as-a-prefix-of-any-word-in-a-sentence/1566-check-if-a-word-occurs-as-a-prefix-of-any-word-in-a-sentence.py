class Solution:
    def isPrefixOfWord(self, s: str, t: str) -> int:
        s=' '+s
        t=' '+t
        n, m=len(s), s.find(t)
        if m==-1: return -1
        return 1+s[:m].count(' ')
        
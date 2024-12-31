class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = sorted(ransomNote)
        m = sorted(magazine)
        
        idx = 0
        for char in m:
            if idx < len(r) and r[idx] == char:
                idx += 1
        
        return idx == len(r)
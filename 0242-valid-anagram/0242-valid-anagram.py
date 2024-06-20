class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return Ture
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        
        if sorted_s == sorted_t:
            return True
        else:
            return False

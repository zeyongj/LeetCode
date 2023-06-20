class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        pos = len(s) - 1
        
        while pos >= 0 and s[pos] == " ":
            pos -= 1
        
        while pos >= 0 and s[pos] != " ":
            pos -= 1
            length += 1
        
        return length
        
        
        
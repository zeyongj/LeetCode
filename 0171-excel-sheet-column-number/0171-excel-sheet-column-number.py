class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle)
        
        if size == 0:
            return 0
        
        ans = 0
        digit = 0
        while digit < size:
            ans = ans * 26 + (ord(columnTitle[digit]) - 64)
            digit += 1
        
        return ans
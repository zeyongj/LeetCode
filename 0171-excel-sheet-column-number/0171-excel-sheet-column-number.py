class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle)
        
        if size == 0:
            return 0
        
        ans = 0
        # digit = 0
        # while digit < size:
        #     ans = ans * 26 + (ord(columnTitle[digit]) - 64)
        #     digit += 1
        
        for digit, char in enumerate(reversed(columnTitle)):
            num = ord(char) - 64
            ans += num * (26 ** digit)
        
        return ans
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle)
        
        if size == 0:
            return 0
        
        ans = 0
        index = 0
        while index < size:
            power = size - index - 1
            ans += (26 ** power) * (ord(columnTitle[index]) - 64)
            index += 1
        
        
        
        # for digit, char in enumerate(reversed(columnTitle)):
        #     num = ord(char) - 64
        #     ans += num * (26 ** digit)
        
        return ans
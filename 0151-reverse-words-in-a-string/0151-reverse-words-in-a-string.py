class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1
        
        return output
            
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1
            
    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0
        
        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1
                
    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)
        self.reverse(l, 0, len(l) - 1)
        self.reverse_each_word(l)
        
        return ''.join(l)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        title = 0
        for i in columnTitle:
            current = ord(i)-64 
            title = 26 * title + current
        return title
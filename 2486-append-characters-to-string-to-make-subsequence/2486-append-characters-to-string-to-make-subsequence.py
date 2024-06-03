class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        first = 0
        longest_prefix = 0

        while first < len(s) and longest_prefix < len(t):
            if s[first] == t[longest_prefix]:
                longest_prefix += 1
            first += 1

        return len(t) - longest_prefix
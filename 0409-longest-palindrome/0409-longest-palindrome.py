class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency_map = {}
        for c in s:
            if c not in frequency_map.keys():
                frequency_map[c] = 1
            else:
                frequency_map[c] += 1

        res = 0
        has_odd_frequency = False
        for freq in frequency_map.values():
            if (freq % 2) == 0:
                res += freq
            else:
                res += freq - 1
                has_odd_frequency = True

        if has_odd_frequency:
            return res + 1

        return res
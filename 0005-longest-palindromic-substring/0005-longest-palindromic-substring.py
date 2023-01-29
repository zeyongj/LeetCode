class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        start, length = 0, 1
        for i in range(n):
            j, k = i, i
            while k < n - 1 and s[k + 1] == s[k]:
                k += 1
            i = k + 1
            while j > 0 and k < n - 1 and s[j - 1] == s[k + 1]:
                j -= 1
                k += 1
            new_len = k - j + 1
            if new_len > length:
                start = j
                length = new_len
        return s[start:start + length]

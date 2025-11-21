class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        # find first & last
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        res = 0

        for c in range(26):
            L, R = first[c], last[c]
            if R - L < 2:
                continue

            seen = [False] * 26

            for i in range(L + 1, R):
                idx = ord(s[i]) - ord('a')
                if not seen[idx]:
                    seen[idx] = True
                    res += 1

        return res
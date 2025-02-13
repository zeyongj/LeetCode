class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = (n + 1) * n // 2
        count = Counter()
        i = 0
        for j in range(n):
            count[s[j]] += 1
            while count[s[j]] >= k:
                count[s[i]] -= 1
                i += 1
            res -= j - i + 1
        return res
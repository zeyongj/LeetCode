class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def kmp(s):
           dp = [0] * len(s)
           for i in range(1, len(s)):
               cur = dp[i - 1]
               while cur and s[i] != s[cur]:
                   cur = dp[cur - 1]
               dp[i] = cur + (s[i] == s[cur])
           return dp

        n, la, lb = len(s), len(a), len(b)
        v1 = kmp(a + '#' + s)
        v2 = kmp(b + '#' + s)
        ii = [i - la - la for i,v in enumerate(v1) if v >= la]
        jj = [j - lb - lb for j,v in enumerate(v2) if v >= lb]
        res = []
        j = 0
        for i in ii:
            while j < len(jj) and jj[j] < i - k:
                j += 1
            if j < len(jj) and jj[j] <= i + k:
                res.append(i)
        return res
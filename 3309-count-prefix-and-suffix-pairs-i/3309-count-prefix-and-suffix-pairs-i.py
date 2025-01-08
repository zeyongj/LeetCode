class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            s1 = words[i]
            for j in range(i + 1, n):
                s2 = words[j]
                if len(s2) < len(s1):
                    continue
                pre = s2[:len(s1)]
                suf = s2[-len(s1):]
                if pre == s1 and suf == s1:
                    ans += 1
        return ans
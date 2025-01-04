class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        R = [0] * 26
        for u in s:
            R[ord(u) - ord('a')] += 1
        
        L = [0] * 26
        S = set()
        
        for i in range(len(s)):
            t = ord(s[i]) - ord('a')
            R[t] -= 1
            for j in range(26):
                if L[j] > 0 and R[j] > 0:
                    S.add(26 * t + j)
            L[t] += 1
        
        return len(S)
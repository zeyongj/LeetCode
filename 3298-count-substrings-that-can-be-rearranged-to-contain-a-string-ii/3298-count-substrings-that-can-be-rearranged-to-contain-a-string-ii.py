class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freq = Counter(word2)
        ans = ii = 0 
        cnt = len(word2)
        for ch in word1: 
            if freq[ch] > 0: cnt -= 1
            freq[ch] -= 1
            while cnt == 0: 
                if freq[word1[ii]] == 0: cnt += 1
                freq[word1[ii]] += 1
                ii += 1
            ans += ii 
        return ans 
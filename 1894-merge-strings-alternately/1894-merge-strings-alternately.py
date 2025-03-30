class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=min(len(word1),len(word2))
        v=""
        for i in range (length):
            v+=word1[i]
            v+=word2[i]
        v+=word1[length:]
        v+=word2[length:]
        return v
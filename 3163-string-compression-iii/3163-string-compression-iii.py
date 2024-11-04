class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        cnt, n = 1, len(word)
        ch = word[0]
        for i in range(1, n):
            if word[i] == ch and cnt < 9:
                cnt += 1
            else:
                comp += str(cnt) + ch
                ch = word[i]
                cnt = 1
        comp += str(cnt) + ch
        return comp
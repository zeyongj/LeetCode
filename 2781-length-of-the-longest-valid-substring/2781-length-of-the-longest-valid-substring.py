class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        length = 0
        all = set()
        for s in forbidden:
            all.add(s)
            length = max(length, len(s))
        n = len(word)
        r = 0
        right = n
        for i in range(n - 1, -1, -1):
            if right <= r:
                break
            now = 0
            temp = ''
            for j in range(i, min(right, i + length)):
                temp += word[j]
                if temp in all:
                    right = j
                    break
            r = max(r, right - i)
        return r

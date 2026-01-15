class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True

        total_char_count = sum(len(s) for s in words)

        if total_char_count % len(words) != 0:
            return False

        my_map = [0] * 26
        for s in words:
            for c in s:
                my_map[ord(c) - ord('a')] += 1

        for i in my_map:
            if i % len(words) != 0:
                return False

        return True
                
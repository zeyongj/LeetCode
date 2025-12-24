class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word):
            it = iter(s)
            return all(char in it for char in word)

        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if is_subsequence(word):
                return word

        return ""        
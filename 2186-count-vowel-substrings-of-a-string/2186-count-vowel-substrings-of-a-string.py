class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -2 for v in vowels}
        for i, x in enumerate(word):
            if x not in vowels:
                last_consonant = i
            else:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values())-last_consonant, 0)
        return ans
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        numeric_total = lambda s: int(''.join([str(ord(letter) - ord('a')) for letter in s]))
        return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWord)
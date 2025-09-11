class Solution(object):
    def sortVowels(self, s):
        vowels_set = set("AEIOUaeiou")
        vowels = [c for c in s if c in vowels_set]
        vowels.sort()

        result = []
        it = iter(vowels)

        for c in s:
            result.append(next(it) if c in vowels_set else c)

        return ''.join(result)
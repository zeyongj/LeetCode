class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set('aeiou')
        
        return sum({w[0],w[-1]}.issubset(vowels) for w in words[left:right+1])
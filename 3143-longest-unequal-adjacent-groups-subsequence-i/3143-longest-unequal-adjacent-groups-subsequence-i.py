class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        return [words[0]]+[ words[i+1] for i, (x, y) in enumerate(zip(groups, groups[1:])) if x!=y]
        
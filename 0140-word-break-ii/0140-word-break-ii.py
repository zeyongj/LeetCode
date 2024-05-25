from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]  # Base case: return an empty sentence

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_of_sentences = backtrack(end)
                    for sentence in rest_of_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)  # When sentence is empty, don't add extra space

            memo[start] = sentences
            return sentences

        # Start backtracking from index 0
        return backtrack(0)
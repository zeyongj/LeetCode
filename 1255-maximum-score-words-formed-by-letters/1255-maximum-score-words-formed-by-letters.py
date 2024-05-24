class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Backtracking
        W = len(words)
        # Count how many times each letter occurs
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        # Check if adding this word exceeds the frequency of any letter
        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True
        
        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                # If all words have been iterated, check the score of this subset
                self.max_score = max(self.max_score, total_score)
                return
            # Not adding words[w] to the current subset
            check(w - 1, words, score, subset_letters, total_score)
            # Adding words[w] to the current subset
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                # Consider the next word if this subset is still valid
                check(w - 1, words, score, subset_letters, total_score)
                
            # Rollback effects of this word
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]

        check(W - 1, words, score, subset_letters, 0)
        # Return max_score as the result
        return self.max_score
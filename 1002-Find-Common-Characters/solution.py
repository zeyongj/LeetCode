class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        result = []

        common_character_counts = collections.Counter(words[0])

        for i in range(1, words_size):
            current_character_counts = collections.Counter(words[i])

            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter],
                )

        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result

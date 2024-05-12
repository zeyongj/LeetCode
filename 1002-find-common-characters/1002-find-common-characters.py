class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize character count from the first word
        char_count = {}
        for char in words[0]:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Process the rest of the words
        for word in words[1:]:
            temp_count = {}
            for char in word:
                if char in temp_count:
                    temp_count[char] += 1
                else:
                    temp_count[char] = 1

            for char in list(char_count.keys()): 
                if char in temp_count:
                    char_count[char] = min(char_count[char], temp_count[char])
                else:
                    del char_count[char]

        result = []
        for char, count in char_count.items():
            result.extend([char] * count)
        
        return result

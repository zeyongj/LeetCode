class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        
        if len(seen) == 26:
            return True
        else:
            return False
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)
        for word in words:
            for c in word:
                counts[c] += 1
        
        n = len(words)
        for val in counts.values():
            if val % n != 0:
                return False
        
        return True
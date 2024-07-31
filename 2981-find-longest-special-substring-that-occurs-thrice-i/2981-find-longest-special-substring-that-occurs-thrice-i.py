from itertools import groupby

class Solution:
    def maximumLength(self, s: str) -> int:
        result = -1
        data = Counter()
        for char, it in groupby(s):
            length = sum(1 for _ in it)
            data[(char, length)] += 1
            if length > 1:
                data[(char, length - 1)] += 2
                if length > 2:
                    result = max(result, length - 2)
        
        for (_, length), cnt in data.items():
            if cnt >= 3:
                result = max(result, length)
        return result
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])        
        
        # sum of diff from both sides
        _max = (b - a - 1) + (c - b - 1)

        # insert between
        if b - a == 2 or c - b == 2:
            _min = 1
        else:
            _min = int(b - a > 1) + int(c - b > 1)

        return [_min, _max]
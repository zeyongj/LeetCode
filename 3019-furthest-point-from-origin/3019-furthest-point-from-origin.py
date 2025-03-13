class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        return m.count('_') + abs(m.count('R') - m.count('L'))
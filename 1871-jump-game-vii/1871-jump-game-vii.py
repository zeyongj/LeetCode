import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = collections.deque([0])
        visited, mx = set([0]), 0
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
                if s[j] == '0' and j not in visited:
                    if j == len(s) - 1: return True
                    queue.append(j)
                    visited.add(j)
            mx = max(mx, i + maxJump)
        return False
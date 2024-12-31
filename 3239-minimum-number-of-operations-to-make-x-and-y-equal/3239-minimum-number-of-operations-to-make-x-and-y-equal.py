from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if x <= y:
            return y - x

        q = deque([(x, 0)])
        m = {x: 1}

        while q:
            t = deque()
            while q:
                a, b = q.popleft()
                if a == y:
                    return b

                if a - 1 not in m:
                    t.append((a - 1, b + 1))
                    m[a - 1] = 1

                if a + 1 not in m:
                    t.append((a + 1, b + 1))
                    m[a + 1] = 1

                if a % 5 == 0 and a // 5 not in m:
                    t.append((a // 5, b + 1))
                    m[a // 5] = 1

                if a % 11 == 0 and a // 11 not in m:
                    t.append((a // 11, b + 1))
                    m[a // 11] = 1

            q = t

        return -1

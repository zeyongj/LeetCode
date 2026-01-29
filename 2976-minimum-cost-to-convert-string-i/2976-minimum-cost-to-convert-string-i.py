from typing import List
import math

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:

        INF = math.inf

        # d[i][j] = min cost to convert chr(i) -> chr(j)
        d = [[INF] * 26 for _ in range(26)]

        # same character cost = 0
        for i in range(26):
            d[i][i] = 0

        # fill direct edges
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            d[u][v] = min(d[u][v], w)

        # Floyd–Warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]

        total = 0

        # compute answer
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if d[u][v] == INF:
                return -1
            total += d[u][v]

        return total
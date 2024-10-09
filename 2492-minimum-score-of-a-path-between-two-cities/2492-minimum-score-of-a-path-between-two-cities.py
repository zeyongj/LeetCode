class Solution(object):
    def minScore(self, n, roads):

        p = list(range(n + 1))
        hash = {}

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(x, y, val):
            px = find(x)
            py = find(y)

            a = hash[px] if px in hash else val
            b = hash[py] if py in hash else val
            hash[px] = min(val, a, b)

            if px != py:
                p[py] = px

        for x, y, val in roads:
            union(x, y, val)

        return hash[find(1)]
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return True
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[yr] > self.rank[xr]:
            self.parent[xr] = yr
        else:
            self.parent[xr] = yr
            self.rank[yr] += 1
        return False

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2])
        dsu = DSU(n)
        mst_weights = []

        for u, v, w in edges:
            if not dsu.union(u, v):
                mst_weights.append(w)

        mst_weights.sort(reverse=True)
        for _ in range(min(k - 1, len(mst_weights))):
            mst_weights.pop(0)

        return mst_weights[0] if mst_weights else 0
class UnionFind:
    def __init__(self, n):
        self.parent = [*range(n)]
        self.rank = [1] * n
    
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
        
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1
        return


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        uf = UnionFind(len(source))
        for i, j in allowedSwaps:
            uf.union(i, j)

        components = defaultdict(Counter)
        for i, s in enumerate(source):
            components[uf.find(i)][s] += 1
        cnt = 0
        for i, t in enumerate(target):
            component = uf.find(i)
            if components[component][t] > 0:
                components[component][t] -= 1
            else:
                cnt += 1
        return cnt
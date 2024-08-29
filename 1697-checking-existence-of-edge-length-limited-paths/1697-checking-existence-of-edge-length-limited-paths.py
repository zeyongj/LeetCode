class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        
    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)
        
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        E = len(edgeList)
        Q = len(queries)
        uf = UnionFind(n)
        ans = [False] * Q
        for i in range(Q):
            queries[i].append(i)
        queries.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        j = 0
        for i in range(Q):
            while j < E and edgeList[j][2] < queries[i][2]:
                uf.union(edgeList[j][0], edgeList[j][1])
                j += 1
            ans[queries[i][3]] = (uf.find(queries[i][0]) == uf.find(queries[i][1]))
        return ans

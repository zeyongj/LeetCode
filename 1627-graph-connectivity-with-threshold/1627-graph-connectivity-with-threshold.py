class Solution:
    def findparent(self, node, parent):
        if parent[node] == node:
            return node

        parent[node] = self.findparent(parent[node], parent)
        return parent[node]

    def unionbyrank(self, x, y, parent, rank):
        u = self.findparent(x, parent)
        v = self.findparent(y, parent)

        if rank[u] > rank[v]:
            parent[v] = u
            rank[u] += rank[v]
        elif rank[v] > rank[u]:
            parent[u] = v
            rank[v] += rank[u]
        else:
            parent[v] = u
            rank[u] += rank[v]

    def areConnected(self, n, threshold, queries):
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        for i in range(threshold + 1, n + 1):
            for j in range(2, n // i + 1):
                if self.findparent(i, parent) != self.findparent(j * i, parent):
                    self.unionbyrank(i, i * j, parent, rank)

        q = len(queries)
        ans = [False] * q

        for i in range(q):
            if self.findparent(queries[i][0], parent) == self.findparent(queries[i][1], parent):
                ans[i] = True

        return ans

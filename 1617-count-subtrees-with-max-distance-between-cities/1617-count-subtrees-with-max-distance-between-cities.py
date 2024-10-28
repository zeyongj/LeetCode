class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        def maxDistance(state):  # return: maximum distance between any two cities in our subset. O(n^2)
            cntEdge, cntCity, maxDist = 0, 0, 0
            for i in range(n):
                if (state >> i) & 1 == 0: continue # Skip if city `i` not in our subset
                cntCity += 1
                for j in range(i + 1, n):
                    if (state >> j) & 1 == 0: continue # Skip if city `j` not in our subset
                    cntEdge += dist[i][j] == 1
                    maxDist = max(maxDist, dist[i][j])
            if cntEdge != cntCity - 1: return 0 # Subset form an invalid subtree!
            return maxDist

        INF = n # Since cities form a tree so maximum distance between 2 cities always < n
        dist = [[INF] * n for _ in range(n)]
        for u, v in edges:
            dist[u-1][v-1] = dist[v-1][u-1] = 1
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        ans = [0] * (n - 1)
        for state in range(1, 2**n):
            d = maxDistance(state)
            if d > 0: ans[d - 1] += 1
        return ans
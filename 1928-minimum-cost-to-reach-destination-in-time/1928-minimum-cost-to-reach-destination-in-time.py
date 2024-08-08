class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        n = len(passingFees)

        # adjacency list # TODO: only use shortest path between each pair
        adj = [[] for _ in range(n)]
        for u, v, dt in edges:
            if dt > maxTime: continue
            adj[u].append((v, dt))
            adj[v].append((u, dt))

        # modified Dijkstra
        #    > main idea: explore paths in order by cost
        #    > ideally the minimum cost path satisifes the maxTime limit
        #    > but if not, we'll need to consider more expensive paths
        #       so we also should visit shorter paths as well
        times = [math.inf]*n
        costs = [math.inf]*n
        times[0] = 0
        costs[0] = passingFees[0]
        pq = [(costs[0], times[0], 0)] # explore by cost asc | time <= maxTime
        while pq:
            c, t, u = heappop(pq)

            if u == n-1:
                return c # first encounter of n-1 ord by cost: we found the min cost

            if c > costs[u] and t > times[u]: continue # stale entry in heap

            # this path to u is either the minimum cost, or the minimum time
            # for costs > u as we explore by costs > u
            for v, dt in adj[u]:
                vt = t+dt
                vc = c+passingFees[v]

                if vt > maxTime: continue # illegal path
                
                if vc < costs[v]:
                    # new lowest cost, want to explore all legal paths from here to get the min cost
                    costs[v] = vc
                    heappush(pq, (vc, vt, v))
                elif vt < times[v]:
                    # higher cost than current min-cost path, but less time. worth exploring
                    times[v] = vt
                    heappush(pq, (vc, vt, v))
                # else: neither the best cost nor best time, ignore it

        return -1 # never encountered n-1 via a path of suitable distance
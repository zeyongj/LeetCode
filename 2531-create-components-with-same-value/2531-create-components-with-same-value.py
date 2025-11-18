class Solution:
    def componentValue(self, N:List[int], E: List[List[int]]) -> int:
        ma, ss, n = max(N), sum(N), len(N)
        G = collections.defaultdict(set)
        degree = [0] * n
        for a, b in E:
            degree[a] += 1
            degree[b] += 1
            G[a].add(b)
            G[b].add(a)
            
        def bfs(target):
            V, deg = N[:], degree[:]
            dq = collections.deque([i for i, d in enumerate(degree) if d == 1])
            
            while dq:
                ci = dq.popleft()
                deg[ci] = 0
                for nxt in G[ci]:
                    if V[ci] != target: V[nxt] += V[ci] # Edge case 1.
                    deg[nxt] -= 1
                    if deg[nxt] == 0:
                        return V[nxt] == target # Edge case 3.
                    elif deg[nxt] == 1:
                        dq.append(nxt)     
           
        for cand in range(min(N), ss):
            if ss % cand == 0 and bfs(cand):
                return ss // cand - 1
        return 0
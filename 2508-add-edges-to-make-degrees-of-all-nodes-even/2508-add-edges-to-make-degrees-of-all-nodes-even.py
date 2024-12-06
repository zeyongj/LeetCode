class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        def check(u,v):
            return u not in adj[v]

        adj = [set() for _ in range(n+1)]

        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        odd = [node for node in range(1,n+1) if len(adj[node])%2 == 1]

        count = len(odd)

        if count == 0:
            return True
        elif count == 2:
            a,b = odd
            return any( check(a,other) and check(b,other) for other in range(1,n+1) )
        elif count == 4:
            a,b,c,d = odd
            ans = False
            ans = ans or check(a,b) and check(c,d)
            ans = ans or check(a,c) and check(b,d)
            ans = ans or check(a,d) and check(b,c)
            return ans
        return False
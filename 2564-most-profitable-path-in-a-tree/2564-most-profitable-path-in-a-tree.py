class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n=len(edges)+1
        adj=[[] for _ in range(n)]
        parent=[-1]*n
        Bob=[float('inf')]*n 

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: Build parent information using DFS
        def dfs(i, p):
            parent[i] = p
            for j in adj[i]:
                if j == p: continue
                dfs(j, i)

        dfs(0, -1)  # Start with -1 as the parent of root

        # Step 2: Compute Bob's arrival times
        x=bob
        move=0
        while x!=-1:
            Bob[x]=move
            move+=1
            x=parent[x]

        # Step 3: DFS to compute Alice's best profit path
        def dfs_sum(i, dist, prev):
            alice=0
            if dist < Bob[i]:
                alice=amount[i]  # Alice takes full amount
            elif dist==Bob[i]:
                alice=amount[i]//2  # Both reach at the same time

            isLeaf=True
            maxLeafSum=-float('inf')

            for j in adj[i]:
                if j == prev: continue
                isLeaf=False
                maxLeafSum = max(maxLeafSum, dfs_sum(j, dist+1, i))

            return alice if isLeaf else alice + maxLeafSum

        return dfs_sum(0, 0, -1)
    
        
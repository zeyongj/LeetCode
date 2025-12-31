class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n=len(cells)+2
        root=[i for i in range(n)]
        rank=[1]*n
        isWater=[False]*n

        def Find(x):
            if x!=root[x]:
                root[x]=Find(root[x])
            return root[x]
        def Union(x, y):
            x, y=Find(x), Find(y)
            if x==y: return
            if rank[x]>rank[y]: x, y=y, x
            root[x]=y
            if rank[x]==rank[y]: rank[y]+=1
        def connected(x, y):
            return Find(x)==Find(y)
        def key(i, j):
            return (i-1)*col+j-1
        East, West=n-2, n-1
        for t, (i, j) in enumerate(cells):
            idx0=key(i,j)
            isWater[idx0]=True
            if j==1: Union(West, idx0)
            if j==col: Union(East, idx0)
            adj=((i+1, j-1), (i+1, j), (i+1, j+1), 
                (i, j+1), (i-1, j+1), (i-1, j), (i-1, j-1), (i, j-1))
            for a, b in adj:
                if a<=0 or a>row or b<=0 or b>col: continue
                idx1=key(a, b)
                if not isWater[idx1]: continue
                Union(idx0, idx1)
                if connected(East, West): return t
        return 0


        
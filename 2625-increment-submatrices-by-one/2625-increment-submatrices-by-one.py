class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        arr=[[0]*n for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            arr[r1][c1]+=1
            arr[r2+1][c1]-=1
            if c2+1<n:
                arr[r1][c2+1]-=1
                arr[r2+1][c2+1]+=1
        for i in range(n):
            arr[i]=list(accumulate(arr[i]))
        for j in range(n):
            for i in range(1, n):
                arr[i][j]+=arr[i-1][j]
        return arr[:n]
        
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        x2i={}
        dp=[[2]*n for _ in range(n)]
        ans=0

        for i, x in enumerate(arr):
            x2i[x]=i

        for i1 in range(1, n-1):
            f1=arr[i1]
            for i2 in range(i1+1, n):
                f2=arr[i2]
                f0=f2-f1
                if f0>=f1: break
                if f0 in x2i:
                    i0=x2i[f0]
                    dp[i1][i2]=dp[i0][i1]+1
                ans=max(ans, dp[i1][i2])
        return ans if ans>2 else 0
               
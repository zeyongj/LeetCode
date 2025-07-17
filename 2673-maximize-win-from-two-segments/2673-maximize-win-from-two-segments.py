from bisect import bisect_right,bisect_left
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        ans=prv=0
        for i,item in enumerate(prizePositions):
            j1=bisect_left(prizePositions,item-k)
            j2=bisect_right(prizePositions,item+k)
            ans=max(ans,j2-j1,prv+j2-i)
            prv=max(prv,i-j1+1)
        return ans
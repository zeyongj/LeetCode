class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n=len(edges)
        sc=[0]*n
        mx=0
        ans=0
        for i in range(n):
            sc[edges[i]]+=i
            if sc[edges[i]]>mx:
                mx=sc[edges[i]]
                ans=edges[i]
            elif sc[edges[i]]==mx:
                if ans>edges[i]:
                    ans=edges[i]
        return ans

class Solution:
    def numberOfPairs(self, P: List[List[int]]) -> int:
        P.sort(key=lambda p: (-p[0], p[1]))
        n, ans=len(P), 0
        for i in range(n-1):
            y=1<<31
            for j in range(i+1, n):
                if y>P[j][1]>=P[i][1]:
                    ans+=1
                    y=P[j][1]
        return ans
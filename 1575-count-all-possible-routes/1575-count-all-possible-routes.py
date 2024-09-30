class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        Mod=10**9+7
        n=len(locations)
        row=[-1]*(fuel+1)
        dp=[row[:] for _ in range(n)]

        def dfs(i, finish, fuel):
            if fuel<0: return 0
            if dp[i][fuel]!=-1: return dp[i][fuel]
            ans=0
            if i==finish: ans+=1
            for j in range(n):
                if j==i: continue
                ans=(ans+dfs(j, finish, fuel-abs(locations[i]-locations[j])))%Mod
            dp[i][fuel]=ans
            return ans

        return dfs(start, finish, fuel)
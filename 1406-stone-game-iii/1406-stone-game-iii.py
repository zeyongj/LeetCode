class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)

        @cache
        def dfs(idx):
            if idx>=n:
                return 0
            best=-10**20
            s=0
            for i in range(3):
                if (i+idx)>=n:
                    break
                s+=stoneValue[i+idx]
                best=max(best,s-dfs(idx+i+1))
            return best

        relativeRes = dfs(0)
        return "Alice" if relativeRes>0 else ("Tie" if relativeRes==0 else "Bob")
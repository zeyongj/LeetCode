class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        freq=[0]*1001
        Sum, xMin, xMax=0, 1000, 1
        for x in skill:
            freq[x]+=1
            Sum+=x
            xMin=min(xMin, x)
            xMax=max(xMax, x)
        n_2=len(skill)//2
        if Sum%n_2!=0: return -1
        team_skill=Sum//n_2

        chemi=0
        l, r=xMin, xMax
        while l<r:
            fL, fR=freq[l], freq[r]
            if l+r!=team_skill or fL!=fR: return -1
            chemi+=fL*l*r
            l+=1
            r-=1
        if l==r and l*2==team_skill:
            chemi+=freq[l]//2*l*l
        return chemi
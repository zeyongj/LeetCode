class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq=Counter(ranks)
        minR=min(ranks)
    #    maxR=max(ranks) # no need
        def canRepair(t):
            cnt=0
            for x, f in freq.items():
                cnt+=f*(sqrt(t/x)//1)
                if cnt>=cars: return True
            return cnt>=cars
        
        l, r=1, minR*cars*cars
        while l<r:
            m=(l+r)>>1
            if canRepair(m):
                r=m
            else:
                l=m+1
        return l
        
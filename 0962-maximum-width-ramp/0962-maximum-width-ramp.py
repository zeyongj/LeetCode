class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        return max(map(sub,a:=[i for _,i in sorted((v,i) for i,v in enumerate(a))],accumulate(a,min)))
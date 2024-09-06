class Solution:
    def maxWidthRamp(self, a: List[int]) -> int:
        a = [i for _,i in sorted((v,i) for i,v in enumerate(a))]
        b = accumulate(a, min)

        return max(map(sub, a, b))
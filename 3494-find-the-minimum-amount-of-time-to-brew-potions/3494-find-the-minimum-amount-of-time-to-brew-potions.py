class Solution:
    def minTime(self, a: List[int], b: List[int]) -> int:
        q = [0]*(len(a)+1)
        for p in b:
            qq = [0,*accumulate(v*p for v in a)]
            dt = max(map(sub,q[1:],qq))
            q = [t+dt for t in qq]

        return q[-1]
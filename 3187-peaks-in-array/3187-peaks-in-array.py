from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def countOfPeaks(self, a: List[int], q: List[List[int]]) -> List[int]:
        p = SortedList(i for i in range(1, len(a)-1) if a[i-1] < a[i] > a[i+1])
        res = []
        
        for e in q:
            if e[0] == 1:
                l, r = e[1:]
                j1 = bisect_right(p, l)
                j2 = bisect_left(p, r) - 1
                res.append(max(j2 - j1 + 1, 0))
            
            elif e[0] == 2:
                i, v = e[1:]
                a[i] = v
                
                for ii in range(i-1, i+2):
                    p.discard(ii)
                    if 0 < ii < len(a)-1 and a[ii-1] < a[ii] > a[ii+1]:
                        p.add(ii)
        
        return res
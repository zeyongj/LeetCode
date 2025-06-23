class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        x = sorted([(a,b) for a,b in zip(nums1,nums2)], reverse=True)
        q = sorted([(a,b,i) for i,(a,b) in enumerate(queries)], reverse=True)
        i, maxy = 0, 0
        res = defaultdict(int)
        d = []
        for a,b,j in q:
            while i < len(x) and x[i][0] >= a:
                if x[i][1] > maxy:
                    maxy = x[i][1]
                    while d and d[-1][1] < x[i][0]+x[i][1]:
                        d.pop()
                    d.append((maxy, x[i][0]+x[i][1]))
                i += 1
            try:
                res[j] = d[bisect_left(d, (b, 0))][1]
            except:
                res[j] = -1
        return [res[i] for i in range(len(q))]
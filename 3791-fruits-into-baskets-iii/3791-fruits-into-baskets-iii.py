class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        seg = [0] * (4 * n + 1)
        def Update(p):
            seg[p] = max(seg[p << 1], seg[p << 1 | 1])
        def Build(p, l, r):
            if l == r:
                seg[p] = baskets[l]
                return
            mid = (l + r) >> 1
            Build(p << 1, l, mid)
            Build(p << 1 | 1, mid + 1, r)
            Update(p)
        def Assign(x, v, p, l, r):
            if x < l or x > r:
                return
            if l == r:
                seg[p] = v
                return
            mid = (l + r) >> 1
            Assign(x, v, p << 1, l, mid)
            Assign(x, v, p << 1 | 1, mid + 1, r)
            Update(p)
        def FirstLarger(v, p, l, r):
            if seg[p] < v:
                return r + 1
            if l == r:
                return r
            mid = (l + r) >> 1
            lf = FirstLarger(v, p << 1, l, mid)
            if lf <= mid:
                return lf
            return FirstLarger(v, p << 1 | 1, mid + 1, r)
        Build(1, 0, n - 1)
        res = 0
        for x in fruits:
            pos = FirstLarger(x, 1, 0, n - 1)
            if pos == n:
                res += 1
            else:
                Assign(pos, 0, 1, 0, n - 1)
        return res
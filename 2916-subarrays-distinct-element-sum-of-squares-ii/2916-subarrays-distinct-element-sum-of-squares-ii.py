from collections import defaultdict
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = [0]*(4*n)
        lazy = [0]*(4*n)
        def build(tree, arr, v, lo, hi):
            if lo == hi:
                tree[v] = arr[lo]
                return
            m = (lo + hi)//2
            build(tree, arr, 2*v + 1, lo, m)
            build(tree, arr, 2*v + 2, m + 1, hi)
            tree[v] = tree[2*v + 1] + tree[2*v + 2]

        def update(tree, v, lo, hi, i, j, val):
            if lazy[v]:
                tree[v] += (hi - lo + 1) * lazy[v]
                if lo < hi:
                    lazy[2*v + 1] += lazy[v]
                    lazy[2*v + 2] += lazy[v]
                lazy[v] = 0
            if lo > j or hi < i: 
                return 
            if i <= lo and hi <= j:
                tree[v] += (hi - lo + 1)*val
                if lo < hi:
                    lazy[2*v + 1] += val 
                    lazy[2*v + 2] += val
                return
            m = (lo + hi)//2
            update(tree, 2*v + 1, lo, m, i, j, val) 
            update(tree, 2*v + 2, m+1, hi, i, j, val)
            tree[v] = tree[2*v + 1] + tree[2*v + 2]

        def query(tree, v, lo, hi, i, j):
            if j < lo or hi < i:
                return 0
            if lazy[v]:
                tree[v] += (hi - lo + 1)*lazy[v]
                if lo < hi:
                    lazy[2*v + 1] += lazy[v]
                    lazy[2*v + 2] += lazy[v]
                lazy[v] = 0
            if i <= lo and hi <= j:
                return tree[v]
            m = (lo + hi)//2
            if i > m:
                return query(tree, 2*v + 2, m + 1, hi, i, j)
            elif j <= m:
                return query(tree, 2*v + 1, lo, m, i, j)
            return query(tree, 2*v + 1, lo, m, i, m) + query(tree, 2*v + 2, m+1, hi, m+1, j)

        squares = 1
        update(tree, 0, 0, n-1, n-1, n-1, 1)
        index = defaultdict(lambda:n)
        index[nums[-1]] = n - 1
        res = 1
        for i in range(n-2,-1,-1):
            j = index[nums[i]]
            squares += (j-i) + 2*query(tree,0,0,n-1,i+1,j-1)
            res += squares
            update(tree, 0, 0, n-1, i, j-1, 1)
            index[nums[i]] = i
        return res%(10**9 + 7)
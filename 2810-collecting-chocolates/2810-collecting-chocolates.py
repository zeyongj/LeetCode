class Solution:
    def minCost(self, A: List[int], x: int) -> int:
        n = len(A)
        res = [x * k for k in range(n)]
        for i in range(n):
            cur = A[i]
            for k in range(n):
                cur = min(cur, A[i - k])
                res[k] += cur
        return min(res)